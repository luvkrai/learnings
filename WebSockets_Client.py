# WS client example

import asyncio
import websockets

async def hello():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        msg = await websocket.recv()
        print(f"< {msg}")
        msg = await websocket.recv()
        print(f"< {msg}")
        msg = await websocket.recv()
        print(f"< {msg}")
        msg = await websocket.recv()
        print(f"< {msg}")
        msg = await websocket.recv()
        print(f"< {msg}")
asyncio.get_event_loop().run_until_complete(hello())