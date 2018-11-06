# coding: utf-8

"""
@author: 武明辉 
@time: 18-11-1 下午4:17
"""
import doctest

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to 
display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s, numRows):
        # 80 ms
        """
        >>> s = Solution()
        >>> s.convert('PAYPALISHIRING', 3)
        'PAHNAPLSIIGYIR'
        >>> s.convert('PAYPALISHIRING', 4)
        'PINALSIGYAHRPI'
        >>> s.convert('AB', 1)
        'AB'
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        cur = 0
        direct = 0
        for i in range(len(s)):
            rows[cur] += s[i]
            if cur == 0:
                direct = 1
            elif cur == numRows - 1:
                direct = -1
            cur += direct

        return ''.join(rows)


if __name__ == '__main__':
    doctest.testmod()
