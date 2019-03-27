from aiohttp import web


class MyView(web.View):
    async def get(self):
        return await get_resp(self.request)

    async def post(self):
        return await post_resp(self.request)


async def handler(request):
    data = {'some': 'data'}
    return web.json_response(data)


app = web.Application(debug=True)
web.view('/path/to', MyView)
