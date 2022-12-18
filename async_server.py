import asyncio
import websockets
import logging

# async def echo(websocket):
#     async for message in websocket:
#         await websocket.send(message)

# async def main():
#     async with serve(echo, "localhost", 8765):
#         await asyncio.Future()  # run forever



logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()
    
    async def register(self, ws: websockets.WebSocketServerProtocol) -> None:
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects.')
        
    async def unregister(self, ws: websockets.WebSocketServerProtocol) -> None:
        self.clients.remove(websockets)
        logging.info(f'{ws.remote_address} disconnects')
    
    async def send_to_clients(self, msg: str) -> None:
        if self.clients:
            await asyncio.wait([
                client.send(msg) for client in self.clients
            ])
    
    async def distribute(self, ws: websockets.WebSocketServerProtocol) -> None:
        async for msg in ws:
            await self.send_to_clients(msg)
            
    async def ws_handler(self, ws: websockets.WebSocketServerProtocol, uri: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)
            
    
if __name__ == '__main__':
    server = Server()
    start_server = websockets.serve(server.ws_handler, 'localhost', 4000)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()