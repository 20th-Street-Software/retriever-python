# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemorySearchMemoriesParams"]


class MemorySearchMemoriesParams(TypedDict, total=False):
    query: Required[str]
    """Search query text for semantic similarity matching"""

    limit: int
    """Maximum number of results to return"""

    mode: Literal["semantic", "filter", "hybrid"]
    """
    Search mode - semantic uses vector similarity, filter uses exact matching,
    hybrid combines both
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Optional user filter - only return memories for this user"""
