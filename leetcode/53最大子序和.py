from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        tmp = nums[0]
        for i in range(1, len(nums)):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
            mx = max(tmp, mx)
        return mx


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([1]))
