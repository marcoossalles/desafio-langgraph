from google import genai

from app.core.config import settings
from app.core.logger import logger

from app.services.ai.llm_service import LLMService


class GeminiProvider(LLMService):

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def generate_response(
        self,
        message: str
    ) -> str:

        logger.info("llm.gemini.request.started model=%s", settings.LLM_MODEL)

        try:

            response = self.client.models.generate_content(
                model=settings.LLM_MODEL,
                contents=message
            )

        except Exception:

            logger.exception(
                "llm.gemini.request.failed model=%s",
                settings.LLM_MODEL
            )

            raise

        logger.info("llm.gemini.request.completed model=%s", settings.LLM_MODEL)

        return response.text
