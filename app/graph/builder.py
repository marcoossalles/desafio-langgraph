from langgraph.graph import (
    StateGraph,
    END
)

from app.states.agent_state import (
    AgentState
)

from app.graph.nodes.supervisor_node import (
    supervisor_node
)

from app.graph.nodes.agent_executor_node import (
    agent_executor_node
)

from app.graph.nodes.response_node import (
    response_node
)


builder = StateGraph(
    AgentState
)

builder.add_node(
    "supervisor",
    supervisor_node
)

builder.add_node(
    "agent_executor",
    agent_executor_node
)

builder.add_node(
    "response",
    response_node
)

builder.set_entry_point(
    "supervisor"
)

builder.add_edge(
    "supervisor",
    "agent_executor"
)

builder.add_edge(
    "agent_executor",
    "response"
)

builder.add_edge(
    "response",
    END
)

graph = builder.compile()