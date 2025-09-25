# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryStoreConversationResponse"]


class MemoryStoreConversationResponse(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")
    """Unique identifier for the processed conversation"""

    session_id: str = FieldInfo(alias="sessionId")
    """Session identifier used or generated for this conversation"""

    status: Literal["processing"]
    """Current processing status of the conversation"""
