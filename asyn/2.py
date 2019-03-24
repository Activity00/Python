import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    # 总共花费3m顺序执行与3形成对比
    print(f'started as {time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'finished at  {time.strftime("%X")}')

asyncio.run(main())
