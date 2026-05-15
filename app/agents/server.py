from app.agents.registry.agent_registry import (
    AgentRegistry
)

from app.agents.movie.movie_agent import (
    MOVIE_AGENT
)

from app.agents.recommendation.recommendation_agent import (
    RECOMMENDATION_AGENT
)


class AgentServer:

    def __init__(self):

        self.registry = AgentRegistry()

        self._register_agents()

    def _register_agents(self):

        self.registry.register(
            "movie_agent",
            MOVIE_AGENT
        )

        self.registry.register(
            "recommendation_agent",
            RECOMMENDATION_AGENT
        )


agent_server = AgentServer()