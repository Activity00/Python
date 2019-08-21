import asyncio
import time
from asyncio import transports


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.transport = None

    def connection_made(self, transport: transports.BaseTransport) -> None:
        peername = transport.get_extra_info('peername')
        print(f'connect from {peername}')
        self.transport = transport
        self.factory.dt[time.time()] = peername

    def data_received(self, data: bytes) -> None:
        print(self.factory.dt)
        message = data.decode()
        print(f'Data recieved: {message}')
        self.transport.write(data)
        print('close the client socket')
        # self.transport.close()


class EchoFactory:
    def __init__(self):
        self.dt = {}

    def __call__(self, *args, **kwargs):
        return EchoServerProtocol(self)


async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(EchoFactory(), 'localhost', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
