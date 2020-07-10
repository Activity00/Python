"""
输入: 3
输出: [1,3,3,1]
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        t = self.getRow(rowIndex - 1)
        x = []
        for i in range(1, rowIndex + 2):
            if i == 1 or i == rowIndex + 1:
                x.append(1)
            else:
                x.append(t[i - 2] + t[i-1])

        return x


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
