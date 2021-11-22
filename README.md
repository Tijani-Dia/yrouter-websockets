# Yrouter-websockets

`yrouter-websockets` is a URL routing package for the [`websockets`](https://github.com/aaugustin/websockets) library. It's built on top of [`yrouter`](https://github.com/Tijani-Dia/yrouter).

## Example

```python
import asyncio

import websockets

from yrouter import route
from yrouter_websockets import router


async def home(ws):
    await ws.send("In home")


async def hello_user(ws, username):
    await ws.send(f"Hello {username}")


async def channel(ws, channel_id):
    # Do some stuff with channel_id


routes = (
    route("/", home),
    route("hello/<str:username>/", hello_user),
    route("channels/<int:channel_id>", channel),
)


async def main():
    async with websockets.serve(router(routes), "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

```

## Installation

`yrouter-websockets` requires `Python>=3.9`. You can install it from Pypi:

```python
pip install yrouter-websockets
```
