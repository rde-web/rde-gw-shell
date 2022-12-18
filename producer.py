import asyncio
import websockets

async def produce(msg: str, host: str, port: int) -> None:
    async with websockets.connect(f'ws://{host}:{port}') as ws:
        await ws.send(msg)
        await ws.recv()
        
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(produce(msg='ahuet', host='localhost', port=4000))
    