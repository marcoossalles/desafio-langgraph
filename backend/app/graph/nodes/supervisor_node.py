import json

from backend.app.states.agent_state import (
    AgentState
)

from backend.app.core.logger import logger

from backend.app.services.ai.llm_factory import (
    LLMFactory
)

from backend.app.schemas.supervisor_decision_schema import (
    SupervisorDecisionSchema
)

from backend.app.agents.supervisor.prompt import (
    SUPERVISOR_PROMPT
)


async def supervisor_node(
    state: AgentState
):

    logger.info("graph.supervisor.started")

    llm = LLMFactory.get_provider()

    full_prompt = f"""
    {SUPERVISOR_PROMPT}

    User message:
    {state.user_message}
    """

    try:

        response = await (
            llm.generate_response(
                message=full_prompt
            )
        )

        decision_data = json.loads(
            response
        )

        decision = (
            SupervisorDecisionSchema(
                **decision_data
            )
        )

    except json.JSONDecodeError as exc:

        logger.exception(
            "graph.supervisor.invalid_json response=%r",
            response
        )

        raise ValueError(
            "Supervisor returned invalid JSON."
        ) from exc

    except Exception:

        logger.exception("graph.supervisor.failed")

        raise

    state.capability = (
        decision.capability
    )

    state.selected_agents = (
        decision.selected_agents
    )

    logger.info(
        "graph.supervisor.completed capability=%s selected_agents=%s",
        state.capability,
        state.selected_agents
    )

    return state
