import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    # Schedule three calls *concurrently*:
    a, b = factorial("A", 2), factorial("B", 3)
    g = asyncio.gather(a, b)
    print(g.__dict__)
    await g


async def f():
    yield 2

asyncio.run(main())

