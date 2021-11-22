from yrouter import NoMatch, Router


class router(Router):
    async def __call__(self, ws):
        if (match := self.match(ws.path)) is NoMatch:
            return await ws.close(1001, reason="Not Found.")

        return await match.handler(ws, **match.kwargs)
