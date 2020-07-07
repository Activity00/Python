


def top_k(nums, p, r, k):
    q = partition(nums, p, r)

    while q != k - 1:
        if q == k - 1:
            return nums[q]
        elif q > k - 1:
            q = partition(nums, q + 1, r)
        else:
            q = partition(nums, p, q - 1)


if __name__ == '__main__':
    ns = [1, 4, 7, 2, 5, 8]
    x = top_k(ns, 0, len(ns) - 1, 2)
    print(x)
    print(ns)
