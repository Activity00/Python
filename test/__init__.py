import time


def fib_p(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    fib = 0
    cnt = 1
    while cnt < n:
        fib = a + b
        a = b
        b = fib
        cnt += 1
    return fib


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

start = time.time()
#fib(35)
end = time.time() - start
print(end)

start = time.time()
fib_p(100000)
end = time.time() - start
print(end)
