# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemorySearchMemoriesResponse", "Result", "ResultMemory"]


class ResultMemory(BaseModel):
    id: str
    """Unique memory identifier"""

    category: Literal[
        "conversation_history", "working_memory", "attention_context", "factual", "episodic", "semantic", "other"
    ]
    """Category of memory classification"""

    conversation_id: str = FieldInfo(alias="conversationId")
    """Source conversation identifier"""

    created_at: int = FieldInfo(alias="createdAt")
    """Unix timestamp when memory was created"""

    importance: int
    """Importance score of the memory"""

    type: Literal["short_term", "long_term", "other"]
    """Type of memory storage"""

    user_id: str = FieldInfo(alias="userId")
    """User associated with this memory"""


class Result(BaseModel):
    chunk_id: str = FieldInfo(alias="chunkId")
    """Unique identifier for the memory chunk"""

    chunk_index: int = FieldInfo(alias="chunkIndex")
    """Index position of this chunk within the source"""

    content: str
    """Text content of the memory"""

    similarity_score: float = FieldInfo(alias="similarityScore")
    """Similarity score between 0 and 1 indicating relevance to the query"""

    tokens: int
    """Number of tokens in the content"""

    type: Literal["memory"]
    """Type of search result"""

    memory: Optional[ResultMemory] = None

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata about the memory"""


class MemorySearchMemoriesResponse(BaseModel):
    limit: int
    """Limit used for this search"""

    processing_time_ms: float = FieldInfo(alias="processingTimeMs")
    """Time taken to process the query in milliseconds"""

    query: str
    """Original search query"""

    results: List[Result]
    """Array of matching memory search results"""

    total_results: int = FieldInfo(alias="totalResults")
    """Total number of results returned"""
