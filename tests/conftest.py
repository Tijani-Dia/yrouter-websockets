import pytest
import websockets

from yrouter_websockets import router

from .routes import routes


async def echo():
    pass


@pytest.fixture
@pytest.mark.asyncio
async def server():
    async with websockets.serve(router(routes), "localhost", 8765) as s:
        yield s
