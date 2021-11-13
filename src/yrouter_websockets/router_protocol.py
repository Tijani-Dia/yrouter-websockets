import http
from functools import partial

from websockets import WebSocketServerProtocol
from yrouter import NoMatch, Router


class RouterProtocol(WebSocketServerProtocol):
    def __init__(self, *args, router, **kwargs):
        super().__init__(*args, **kwargs)
        self.router = router

    async def process_request(self, path, request_headers):
        match = self.router.match(path)
        if match is NoMatch:
            return (http.HTTPStatus.NOT_FOUND, [], b"Not Found.\n")

        self.ws_handler = partial(match.handler, **match.kwargs)


def router_protocol(routes):
    router = Router(routes)
    return partial(RouterProtocol, router=router)
