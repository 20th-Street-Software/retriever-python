# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retriever import Retriever, AsyncRetriever
from tests.utils import assert_matches_type
from retriever.types import (
    MemorySearchMemoriesResponse,
    MemoryStoreConversationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_memories(self, client: Retriever) -> None:
        memory = client.memory.search_memories(
            query="user preferences for outdoor activities",
        )
        assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_memories_with_all_params(self, client: Retriever) -> None:
        memory = client.memory.search_memories(
            query="user preferences for outdoor activities",
            limit=1,
            mode="semantic",
            user_id="userId",
        )
        assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_memories(self, client: Retriever) -> None:
        response = client.memory.with_raw_response.search_memories(
            query="user preferences for outdoor activities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_memories(self, client: Retriever) -> None:
        with client.memory.with_streaming_response.search_memories(
            query="user preferences for outdoor activities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_store_conversation(self, client: Retriever) -> None:
        memory = client.memory.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
        )
        assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_store_conversation_with_all_params(self, client: Retriever) -> None:
        memory = client.memory.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_store_conversation(self, client: Retriever) -> None:
        response = client.memory.with_raw_response.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_store_conversation(self, client: Retriever) -> None:
        with client.memory.with_streaming_response.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_memories(self, async_client: AsyncRetriever) -> None:
        memory = await async_client.memory.search_memories(
            query="user preferences for outdoor activities",
        )
        assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_memories_with_all_params(self, async_client: AsyncRetriever) -> None:
        memory = await async_client.memory.search_memories(
            query="user preferences for outdoor activities",
            limit=1,
            mode="semantic",
            user_id="userId",
        )
        assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_memories(self, async_client: AsyncRetriever) -> None:
        response = await async_client.memory.with_raw_response.search_memories(
            query="user preferences for outdoor activities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_memories(self, async_client: AsyncRetriever) -> None:
        async with async_client.memory.with_streaming_response.search_memories(
            query="user preferences for outdoor activities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemorySearchMemoriesResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_store_conversation(self, async_client: AsyncRetriever) -> None:
        memory = await async_client.memory.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
        )
        assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_store_conversation_with_all_params(self, async_client: AsyncRetriever) -> None:
        memory = await async_client.memory.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_store_conversation(self, async_client: AsyncRetriever) -> None:
        response = await async_client.memory.with_raw_response.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_store_conversation(self, async_client: AsyncRetriever) -> None:
        async with async_client.memory.with_streaming_response.store_conversation(
            content=[
                {
                    "content": "I love hiking and prefer mountain trails over coastal walks.",
                    "role": "user",
                },
                {
                    "content": "That's great! Mountain trails offer beautiful scenery and fresh air.",
                    "role": "assistant",
                },
            ],
            user_id="user_12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryStoreConversationResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True
