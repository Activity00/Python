from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 1:
            return s
        return self.reverseString(s[1:]) + [s[0]]


if __name__ == '__main__':
    a = ["h","e","l","l","o"]
    s = Solution()
    print(s.reverseString(a))
    print(a)
