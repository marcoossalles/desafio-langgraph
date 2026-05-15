from app.core.config import settings
from app.core.logger import logger
from app.services.ai.llm_service import LLMService

from app.services.ai.providers.gemini_provider import (
    GeminiProvider
)
from app.services.ai.providers.grop_provider import (
    GroqProvider
)


class LLMFactory:

    @staticmethod
    def get_provider() -> LLMService:

        if settings.LLM_PROVIDER == "gemini":
            
            logger.info(
                "llm.provider.selected provider=%s",
                settings.LLM_PROVIDER
            )
            
            return GeminiProvider()
        
        else: 
            logger.info(
                "llm.provider.selected provider=%s",
                settings.LLM_PROVIDER
            )

            return GroqProvider()
