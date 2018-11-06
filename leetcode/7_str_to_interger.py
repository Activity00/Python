# coding: utf-8

"""
@author: 武明辉 
@time: 18-11-6 下午2:27
"""
import doctest
import re

"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as 
possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no 
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
 [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or
  INT_MIN (−2^31) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
"""


class Solution:

    def myAtoi(self, s):
        s = s.strip()
        try:
            val = ''
            for i in range(len(s)):
                if (s[i] in '+-' and i == 0) or '0' <= s[i] <= '9':
                    val += s[i]
                else:
                    break
            val = int(val)
            if val < -2 ** 31:
                return -2 ** 31
            if val > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return val
        except:
            return 0

    p = re.compile('^\s*((-|\+)?\d+)')

    def myAtoi_re(self, s):
        r = Solution.p.search(str)
        if r is not None:
            i = int(r.groups()[0])
            min = -2 ** 31
            if i < min:
                return min
            max = 2 ** 31 - 1
            if i > max:
                return max
            return i
        return 0

    def myAtoi_my(self, s):
        """
        have problem
        :param s:
        :return:
        """
        """
        >>> s = Solution()
        >>> s.myAtoi("42")
        42
        >>> s.myAtoi('   -42')
        -42
        >>> s.myAtoi('4193 with words')
        4193
        >>> s.myAtoi('words and 987')
        0
        >>> s.myAtoi("-91283472332")
        -2147483648
        >>> s.myAtoi('+-2')
        0
        >>> s.myAtoi("   +0 123")
        0
        >>> s.myAtoi("  0000000000012345678")
        12345678
        """
        if '+-' in s or '-+' in s:
            return 0
        stmp = s.strip()
        f = -1 if stmp.startswith('-') else 1
        ret = 0
        first = False
        for i in range(len(stmp)):
            if stmp[i] not in (' ', '+', '-') and not stmp[i].isdigit():
                break
            if first and stmp[i] == ' ':
                return 0
            if stmp[i].isdigit():
                if stmp[i] != '0':
                    first = True
                ret = ret * 10 + int(stmp[i])

        ret = ret * f
        if ret > 2**32:
            return 2**32
        elif ret < -2**32:
            return -2**31
        return ret


if __name__ == '__main__':
    doctest.testmod()

