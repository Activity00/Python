import asyncio


from grpclib.server import Server

from helloworld_pb2 import HelloReply
from helloworld_grpc import GreeterBase


class Greeter(GreeterBase):

    async def SayHello(self, stream):
        request = await stream.recv_message()
        message = 'Hello, {}!'.format(request.name)
        await stream.send_message(HelloReply(message=message))


async def main(*, host='127.0.0.1', port=50051):
    loop = asyncio.get_running_loop()
    server = Server([Greeter()], loop=loop)
    await server.start(host, port)
    print(f'Serving on {host}:{port}')
    await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
