import aiohttp
from aiohttp import web


async def callback(msg):
    print(msg)


async def websocket(session):
    print('xxx')
    async with session.ws_connect('http://127.0.0.1/websocket') as ws:
        async for msg in ws:
            print(msg)
            if msg.type == aiohttp.WSMsgType.TEXT:
                await callback(msg.data)
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break


async def init(app):
    session = aiohttp.ClientSession()
    app['websocket_task'] = app.loop.create_task(websocket(session))

app = web.Application()
app.on_startup.append(init)
