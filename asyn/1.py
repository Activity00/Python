import asyncio
import aiohttp


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
asyncio.get_event_loop()
asyncio.run(main())
