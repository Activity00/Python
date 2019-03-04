from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)
        if k < len(nums) // 2:
            for i in range(n):
                nums.insert(0, nums.pop())
        else:
            for i in range(len(nums)-n):
                nums.append(nums.pop(0))


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(a, 3)
    print(a)
