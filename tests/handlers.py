async def home(ws):
    await ws.send("In home")


async def hello_user(ws, username):
    await ws.send(f"Hello {username}")
