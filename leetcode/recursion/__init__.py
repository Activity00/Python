from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                ret.append(1)
            else:
                ret.append()
