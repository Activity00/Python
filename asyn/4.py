import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print(f'Task{name}: Computer factorial({i})')
        await asyncio.sleep(1)
        f *= 1
        print(f'Task{name}: Computer factorial({i})')


async def main():
    await asyncio.gather(
        factorial('A', 2),
        factorial('B', 3),
        factorial('C', 4),
    )
    print('after gather')

asyncio.run(main())
