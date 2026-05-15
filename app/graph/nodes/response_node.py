import json

from app.states.agent_state import AgentState
from app.core.logger import logger
from app.services.ai.llm_factory import LLMFactory
from app.prompts.tool_calling_prompt import TOOL_CALLING_PROMPT
from app.services.ai.tool_calling_service import ToolCallingService

MAX_ITERATIONS = 5
MAX_MESSAGES = 12


def truncate_messages(messages: list) -> list:
    return messages[-MAX_MESSAGES:]


def simplify_tool_result(result):

    if not isinstance(result, dict):
        return result

    if "cast" in result:

        return {
            "cast": [
                {
                    "name": actor.get("name"),
                    "character": actor.get("character")
                }
                for actor in result.get("cast", [])[:5]
            ]
        }

    if "results" in result:

        return {
            "results": [
                {
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "overview": item.get("overview")
                }
                for item in result.get("results", [])[:3]
            ]
        }

    return result


async def response_node(state: AgentState) -> AgentState:

    logger.info("graph.response.started")

    llm = LLMFactory.get_provider()
    tool_service = ToolCallingService()

    current_tools = (
        state.current_tools
        or state.context_data.get("loaded_tools", {})
    )

    available_tools = list(current_tools.keys())

    logger.info("graph.response.available_tools tools=%s", available_tools)

    tools_description = "\n".join(
        f"Tool Name: {name}\nDescription: {tool.__doc__}"
        for name, tool in current_tools.items()
    )

    prompt = TOOL_CALLING_PROMPT.format(
        tools=tools_description,
        available_tools=available_tools,
    )

    messages = [
        {
            "role": "user",
            "content": state.user_message
        }
    ]

    for iteration in range(MAX_ITERATIONS):

        logger.info("graph.response.iteration.started iteration=%s", iteration + 1)

        messages = truncate_messages(messages)

        try:

            response = await llm.generate_response(
                message=(
                    f"{prompt}\n\n"
                    f"Conversation:\n"
                    f"{json.dumps(messages, ensure_ascii=False)}"
                )
            )

        except Exception:

            logger.exception(
                "graph.response.llm_failed iteration=%s",
                iteration + 1
            )

            state.final_response = (
                "Erro ao gerar resposta do modelo."
            )

            return state

        logger.info(
            "graph.response.llm_response_received iteration=%s response=%r",
            iteration + 1,
            response
        )

        try:

            parsed_response = json.loads(response)

        except json.JSONDecodeError as e:

            logger.exception(
                "graph.response.invalid_json iteration=%s response=%r",
                iteration + 1,
                response
            )

            state.final_response = (
                "Erro ao processar resposta do modelo."
            )

            return state

        response_type = parsed_response.get("type")

        if response_type == "final_response":

            state.final_response = parsed_response.get(
                "response",
                "Sem resposta."
            )

            return state

        if response_type == "tool_call":

            tool_name = parsed_response.get("tool")
            arguments = parsed_response.get("arguments", {})

            tool = current_tools.get(tool_name)

            if not tool:

                logger.warning(
                    "graph.response.tool_not_found tool=%s available_tools=%s",
                    tool_name,
                    available_tools
                )

                messages.append({
                    "role": "system",
                    "content": (
                        f"Tool '{tool_name}' does not exist.\n"
                        f"You MUST use ONLY one of these tools: "
                        f"{available_tools}"
                    )
                })

                continue

            logger.info(
                "graph.response.tool_call.started tool=%s arguments=%s",
                tool_name,
                arguments
            )

            try:

                result = await tool_service.execute_tool(
                    tool=tool,
                    arguments=arguments
                )

                simplified_result = simplify_tool_result(
                    result
                )

                logger.info(
                    "graph.response.tool_call.completed tool=%s",
                    tool_name
                )

            except Exception as e:

                logger.exception(
                    "graph.response.tool_call.failed tool=%s arguments=%s",
                    tool_name,
                    arguments
                )

                messages.append({
                    "role": "system",
                    "content": (
                        f"Tool execution failed:\n{e}"
                    )
                })

                continue

            messages.append({
                "role": "assistant",
                "content": response
            })

            messages.append({
                "role": "tool",
                "content": json.dumps(
                    simplified_result,
                    ensure_ascii=False
                )
            })

            continue

        logger.warning(
            "graph.response.unknown_response_type type=%s",
            response_type
        )

        messages.append({
            "role": "system",
            "content": (
                "Invalid response type.\n"
                "You MUST return: "
                "tool_call or final_response"
            )
        })

    state.final_response = (
        "Não foi possível concluir a resposta."
    )

    logger.warning(
        "graph.response.max_iterations_reached max_iterations=%s",
        MAX_ITERATIONS
    )

    return state
