# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import memory_search_memories_params, memory_store_conversation_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.memory_search_memories_response import MemorySearchMemoriesResponse
from ..types.memory_store_conversation_response import MemoryStoreConversationResponse

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/20th-Street-Software/retriever-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/20th-Street-Software/retriever-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def search_memories(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        mode: Literal["semantic", "filter", "hybrid"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchMemoriesResponse:
        """
        Performs semantic search across stored memories and returns relevant results.
        Uses vector similarity to find the most relevant user memories extracted from
        conversations.

        Args:
          query: Search query text for semantic similarity matching

          limit: Maximum number of results to return

          mode: Search mode - semantic uses vector similarity, filter uses exact matching,
              hybrid combines both

          user_id: Optional user filter - only return memories for this user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/memory/query",
            body=maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "mode": mode,
                    "user_id": user_id,
                },
                memory_search_memories_params.MemorySearchMemoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchMemoriesResponse,
        )

    def store_conversation(
        self,
        *,
        content: Iterable[memory_store_conversation_params.Content],
        user_id: str,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStoreConversationResponse:
        """Processes a conversation and triggers memory extraction workflow.

        Automatically
        extracts user facts from conversation messages and makes them searchable through
        semantic search.

        Args:
          content: Array of messages in the conversation

          user_id: External user identifier

          session_id: Optional session identifier for grouping related conversations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/memory",
            body=maybe_transform(
                {
                    "content": content,
                    "user_id": user_id,
                    "session_id": session_id,
                },
                memory_store_conversation_params.MemoryStoreConversationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStoreConversationResponse,
        )


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/20th-Street-Software/retriever-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/20th-Street-Software/retriever-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def search_memories(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        mode: Literal["semantic", "filter", "hybrid"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchMemoriesResponse:
        """
        Performs semantic search across stored memories and returns relevant results.
        Uses vector similarity to find the most relevant user memories extracted from
        conversations.

        Args:
          query: Search query text for semantic similarity matching

          limit: Maximum number of results to return

          mode: Search mode - semantic uses vector similarity, filter uses exact matching,
              hybrid combines both

          user_id: Optional user filter - only return memories for this user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/memory/query",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "mode": mode,
                    "user_id": user_id,
                },
                memory_search_memories_params.MemorySearchMemoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchMemoriesResponse,
        )

    async def store_conversation(
        self,
        *,
        content: Iterable[memory_store_conversation_params.Content],
        user_id: str,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryStoreConversationResponse:
        """Processes a conversation and triggers memory extraction workflow.

        Automatically
        extracts user facts from conversation messages and makes them searchable through
        semantic search.

        Args:
          content: Array of messages in the conversation

          user_id: External user identifier

          session_id: Optional session identifier for grouping related conversations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/memory",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "user_id": user_id,
                    "session_id": session_id,
                },
                memory_store_conversation_params.MemoryStoreConversationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryStoreConversationResponse,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.search_memories = to_raw_response_wrapper(
            memory.search_memories,
        )
        self.store_conversation = to_raw_response_wrapper(
            memory.store_conversation,
        )


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.search_memories = async_to_raw_response_wrapper(
            memory.search_memories,
        )
        self.store_conversation = async_to_raw_response_wrapper(
            memory.store_conversation,
        )


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.search_memories = to_streamed_response_wrapper(
            memory.search_memories,
        )
        self.store_conversation = to_streamed_response_wrapper(
            memory.store_conversation,
        )


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.search_memories = async_to_streamed_response_wrapper(
            memory.search_memories,
        )
        self.store_conversation = async_to_streamed_response_wrapper(
            memory.store_conversation,
        )
