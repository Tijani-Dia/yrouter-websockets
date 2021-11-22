import re

import pytest
import websockets
from websockets.exceptions import ConnectionClosedOK

uri = "ws://127.0.0.1:8765"


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
    expected = (
        "received 1001 (going away) Not Found.; "
        "then sent 1001 (going away) Not Found."
    )

    async with websockets.connect(f"{uri}/404/") as ws:
        with pytest.raises(ConnectionClosedOK, match=re.escape(expected)):
            await ws.recv()
