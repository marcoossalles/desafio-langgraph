from fastapi import APIRouter, HTTPException

from backend.app.schemas.chat_schema import (
    ChatRequest
)

from backend.app.states.agent_state import (
    AgentState
)

from backend.app.core.logger import logger

from backend.app.graph.builder import (
    graph
)

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    logger.info("chat.request.received message=%r", request.message)

    state = AgentState(
        user_message=request.message
    )

    try:

        result = await graph.ainvoke(
            state
        )

    except Exception as exc:

        logger.exception(
            "chat.request.failed message=%r",
            request.message
        )

        raise HTTPException(
            status_code=500,
            detail="Erro ao processar mensagem."
        ) from exc

    logger.info("chat.request.completed")

    return result
