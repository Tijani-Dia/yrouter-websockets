import pytest
import websockets
from websockets.exceptions import InvalidStatusCode

uri = "ws://127.0.0.1:8765"


async def echo(websocket):
    pass


@pytest.mark.asyncio
async def test_home(server):
    async with websockets.connect(uri) as ws:
        assert await ws.recv() == "In home"


@pytest.mark.asyncio
async def test_username(server):
    username = "websockets"
    async with websockets.connect(f"{uri}/hello/{username}/") as ws:
        assert await ws.recv() == f"Hello {username}"


@pytest.mark.asyncio
async def test_404(server):
    expected = "server rejected WebSocket connection: HTTP 404"
    with pytest.raises(InvalidStatusCode, match=expected):
        async with websockets.connect(f"{uri}/405/"):
            pass
