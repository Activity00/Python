mp = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}


def custom_hex(num, n):
    x = []
    a = num
    while a != 0:
        a, b = divmod(a, n)
        b = mp.get(b) or b
        x.insert(0, str(b))
    return ''.join(x)


if __name__ == '__main__':
    print(custom_hex(1234, 16))
    print(hex(1234))
