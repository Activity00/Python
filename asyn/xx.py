import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url, headers=headers) as resp:
        print(await resp.json())


async def fetch_main():
    async with aiohttp.ClientSession() as session:
        contract = '0xd6aD7a6750A7593E092a9B218d66C0A814a3436e'
        url = f'https://www.oklink.com/api/explorer/v1/eth/addresses/{contract}/holders'
        task1 = asyncio.ensure_future(fetch(session, url))
        task2 = asyncio.ensure_future(fetch(session, url))
        await task1
        await task2


if __name__ == '__main__':
    headers = {'x-apiKey': 'cbb6a668-f750-486d-a139-0e1286c4a0e3'}
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_main())
