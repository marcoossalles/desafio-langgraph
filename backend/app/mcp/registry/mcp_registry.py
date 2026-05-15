class MCPRegistry:

    def __init__(self):

        self.mcps = {}

    def register(
        self,
        name: str,
        mcp
    ):

        self.mcps[name] = mcp

    def get_mcp(
        self,
        name: str
    ):

        return self.mcps.get(name)

    def get_all_mcps(self):

        return self.mcps