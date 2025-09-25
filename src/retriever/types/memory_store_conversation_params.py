# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryStoreConversationParams", "Content"]


class MemoryStoreConversationParams(TypedDict, total=False):
    content: Required[Iterable[Content]]
    """Array of messages in the conversation"""

    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]
    """External user identifier"""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Optional session identifier for grouping related conversations"""


class Content(TypedDict, total=False):
    content: Required[str]
    """Content of the message"""

    role: Required[Literal["user", "assistant", "system", "function", "tool"]]
    """Role of the message sender"""
