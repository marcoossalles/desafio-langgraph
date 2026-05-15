from pydantic import BaseModel


class SupervisorDecisionSchema(
    BaseModel
):

    capability: str

    selected_agents: list[str]