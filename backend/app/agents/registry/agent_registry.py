class AgentRegistry:

    def __init__(self):

        self.agents = {}

    def register(
        self,
        name: str,
        agent
    ):

        self.agents[name] = agent

    def get_agent(
        self,
        name: str
    ):

        return self.agents.get(name)

    def get_all_agents(self):

        return self.agents