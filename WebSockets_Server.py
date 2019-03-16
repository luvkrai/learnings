# WS server example
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    greeting = f"{name} do you love me?"
    await websocket.send(greeting)
    print(f"> {greeting}")
    loop = asyncio.get_event_loop()
    await websocket.send("Are you riding?")
    await websocket.send("Say you never ever leave from beside me!")
    data = await loop.run_in_executor(None, get_data)
    #data = await get_data()
    await websocket.send("Sending lots of love!!")
    await websocket.send(data)


def get_data():
    # something that takes a long time to calculate
    x = 19134702400093278081449423917**300000 % 256
    return '\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)])
start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()