import asyncio
import logging
import websockets
import subprocess

logging.basicConfig(level=logging.INFO)

async def consumer_handler(websocket: websockets.WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)
        call_command(message)
        
async def consume(hostname: str, port: int) -> None:
    websocket_resource_url = f'ws://{hostname}:{port}'
    async with websockets.connect(
        websocket_resource_url) as websocket:
        await consumer_handler(websocket)
        
def call_command(msg: str) -> None:
    shell_call_result = subprocess.check_output(
        msg, stderr=subprocess.STDOUT, shell=True
    )
    print(f'result : {shell_call_result.decode()}')
        
def log_message(msg: str) -> None:
    logging.info(f'received command >>> {msg}')
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume(hostname='localhost', port=4000))
    loop.run_forever()