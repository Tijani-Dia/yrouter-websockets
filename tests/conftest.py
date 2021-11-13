import pytest
import websockets

from src.yrouter_websockets import router_protocol

from .routes import routes


async def echo():
    pass


@pytest.fixture
@pytest.mark.asyncio
async def server():
    async with websockets.serve(
        echo, "localhost", 8765, create_protocol=router_protocol(routes)
    ) as s:
        yield s
