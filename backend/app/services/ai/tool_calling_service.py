from backend.app.core.logger import logger


class ToolCallingService:

    async def execute_tool(
        self,
        tool,
        arguments: dict
    ):

        logger.info(
            "tool.execution.started tool=%s arguments=%s",
            tool.__name__,
            arguments
        )

        try:

            result = await tool(
                **arguments
            )

        except Exception:

            logger.exception(
                "tool.execution.failed tool=%s arguments=%s",
                tool.__name__,
                arguments
            )

            raise

        logger.info("tool.execution.completed tool=%s", tool.__name__)

        return result
