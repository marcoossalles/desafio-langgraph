from backend.app.states.agent_state import (
    AgentState
)

from backend.app.core.logger import logger

from backend.app.agents.server import (
    agent_server
)

from backend.app.mcp.server import (
    mcp_server
)

async def agent_executor_node(
    state: AgentState
):

    logger.info(
        "graph.agent_executor.started selected_agents=%s",
        state.selected_agents
    )

    loaded_tools = {}

    for agent_name in (
        state.selected_agents
    ):

        agent = (
            agent_server
            .registry
            .get_agent(agent_name)
        )

        if not agent:

            logger.warning(
                "graph.agent_executor.agent_not_found agent=%s",
                agent_name
            )

            continue

        logger.info(
            "graph.agent_executor.agent_started agent=%s",
            agent_name
        )

        for mcp_name in (
            agent["allowed_mcps"]
        ):

            mcp = (
                mcp_server
                .registry
                .get_mcp(mcp_name)
            )

            if not mcp:

                logger.warning(
                    "graph.agent_executor.mcp_not_found mcp=%s agent=%s",
                    mcp_name,
                    agent_name
                )

                continue

            mcp_tools = (
                mcp.get_tools()
            )

            for tool_name in (
                agent["allowed_tools"]
            ):

                if tool_name in mcp_tools:

                    loaded_tools[
                        tool_name
                    ] = mcp_tools[
                        tool_name
                    ]

                    logger.info(
                        "graph.agent_executor.tool_loaded tool=%s agent=%s mcp=%s",
                        tool_name,
                        agent_name,
                        mcp_name
                    )

    state.context_data[
        "loaded_tools"
    ] = loaded_tools

    logger.info(
        "graph.agent_executor.completed loaded_tools=%s",
        list(loaded_tools.keys())
    )

    return state
