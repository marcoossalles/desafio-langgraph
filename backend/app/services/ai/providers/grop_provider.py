from openai import OpenAI

from backend.app.core.config import settings
from backend.app.core.logger import logger

from backend.app.services.ai.llm_service import LLMService


class GroqProvider(LLMService):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

    async def generate_response(
        self,
        message: str
    ) -> str:

        logger.info("llm.groq.request.started model=%s", settings.LLM_MODEL)

        try:

            response = self.client.chat.completions.create(
                model=settings.LLM_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

        except Exception:

            logger.exception(
                "llm.groq.request.failed model=%s",
                settings.LLM_MODEL
            )

            raise

        logger.info("llm.groq.request.completed model=%s", settings.LLM_MODEL)

        return response.choices[0].message.content
