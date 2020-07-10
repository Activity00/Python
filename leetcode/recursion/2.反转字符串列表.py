from typing import List

"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rev(p, r, s):
            if p > r:
                return
            s[p], s[r] = s[r], s[p]
            rev(p+1, r-1, s)

        rev(0, len(s) - 1, s)


if __name__ == '__main__':
    so = Solution()
    x = ["H", "a", "n", "n", "a", "h"]
    so.reverseString(x)
    print(x)
