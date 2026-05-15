from backend.app.mcp.registry.mcp_registry import (
    MCPRegistry
)

from backend.app.mcp.movie_mcp.server import (
    MovieMCP
)


class MCPServer:

    def __init__(self):

        self.registry = MCPRegistry()

        self._register_mcps()

    def _register_mcps(self):

        self.registry.register(
            "movie_mcp",
            MovieMCP()
        )


mcp_server = MCPServer()