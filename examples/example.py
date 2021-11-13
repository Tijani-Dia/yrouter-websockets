import asyncio
import http

import websockets
from yrouter import route

from yrouter_websockets import router_protocol


async def home(ws):
    await ws.send("In home")


async def hello_user(ws, username):
    await ws.send(f"Hello {username}")


async def health_check(ws):
    return http.HTTPStatus.OK, [], b"OK\n"


routes = (
    route("/", home),
    route("hello/<str:username>/", hello_user),
    route("health/", health_check),
)


async def main():
    async with websockets.serve(
        lambda: None, "localhost", 8765, create_protocol=router_protocol(routes)
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
