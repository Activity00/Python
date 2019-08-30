
def permutation(chars, start, end):
    if start == end:
        print(chars)
    else:
        for i in range(start, end):
            chars[i], chars[start] = chars[start], chars[i]
            permutation(chars, start+1, end)
            chars[i], chars[start] = chars[start], chars[i]


def test():
    chars = ['a', 'b', 'c', 'd', 'e']
    permutation(chars, 0, len(chars))


if __name__ == '__main__':
    test()
