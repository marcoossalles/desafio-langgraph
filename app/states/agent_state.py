from pydantic import BaseModel


class AgentState(BaseModel):

    user_message: str

    capability: str | None = None

    selected_agents: list[str] = []

    current_tools: dict = {}

    tool_calls: list[dict] = []

    tool_results: list[dict] = []

    messages: list[dict] = []

    context_data: dict = {}

    final_response: str | None = None