from typing import List


class Solution:
    # my 1400ms
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
            i += 1

    def moveZeroes2(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            i = 0
            s = 0
            for k in nums:
                if k == 0:
                    s += 1
            while i < len(nums) - s:
                if nums[i] == 0:
                    nums.append(0)
                    nums.pop(i)
                    continue
                i += 1


if __name__ == '__main__':
    s = Solution()
    lt = [0, 1, 0, 3, 12]
    s.moveZeroes(lt)
    print(lt)

