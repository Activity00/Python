def merge(nums1, nums2):
    count = len(nums1) + len(nums2)
    ret = [0] * count
    nums1.append(float('inf'))
    nums2.append(float('inf'))
    i = j = 0
    for k in range(count):
        if nums1[i] > nums2[j]:
            ret[k] = nums2[j]
            j += 1
        else:
            ret[k] = nums1[i]
            i += 1
    return ret


def test():
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]
    c = merge(a, b)
    print(c)


if __name__ == '__main__':
    test()
