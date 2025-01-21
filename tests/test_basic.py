import asyncio
import pytest


@pytest.mark.asyncio
async def test_example():
    async def example():
        await asyncio.sleep(1)
        return "Hello, World!"

    result = await example()
    assert result == "Hello, World!"
