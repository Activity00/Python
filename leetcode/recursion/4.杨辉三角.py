"""
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 0:
            return []
        else:
            t = self.generate(numRows - 1)
            x = []
            for i in range(1, numRows + 1):
                if i == 1 or i == numRows:
                    x.append(1)
                else:
                    x.append(t[numRows - 2][i - 2] + t[numRows - 2][i-1])

            t.append(x)
            return t


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
