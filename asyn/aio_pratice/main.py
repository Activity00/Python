import logging

from aiohttp import web

from .routers import setup_routes
from .chat.views import WebSocket
from .auth.views import Login


routes = [
    ('GET', '/',        ChatList,  'main'),
    ('GET', '/ws',      WebSocket, 'chat'),
    ('*',   '/login',   Login,     'login'),
    ('*',   '/signin',  SignIn,    'signin'),
    ('*',   '/signout', SignOut,   'signout'),
]

for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

app.client = ma.AsyncIOMotorClient(MONGO_HOST)
app.db = app.client[MONGO_DB_NAME]


async def setup_db(app, conf, loop):
    # pool = await init_redis(conf['redis'], loop)
    #
    # async def close_redis(app):
    #     pool.close()
    #     await pool.wait_closed()
    #
    # app.on_cleanup.append(close_redis)
    # app['redis_pool'] = pool
    # return pool
    pass


def main():
    logging.basicConfig(level=logging.DEBUG)
    # 1.加载配置
    #  conf = load_config()

    # loop = asyncio.get_event_loop()
    app = web.Application()  # loop=loop
    # app.middlewares = [session_middleware(EncryptedCookieStorage(SECRET_KEY)), authorize, db_handler, ]

    # 2. 初始化数据库连接池等
    # redis_pool = await setup_db(app, conf, loop)

    handler = SiteHandler(redis_pool, conf)

    setup_routes(app, handler, PROJ_ROOT)

    web.run_app(app, host='localhost', port=8888)


if __name__ == '__main__':
    main()
