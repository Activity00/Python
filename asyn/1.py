import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    loop.stop()


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
