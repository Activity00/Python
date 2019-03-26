"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        t = []
        for i in s:
            if i in m.values():
                t.append(i)
            else:
                if i in m.keys() and t and m[i] == t[-1]:
                    t.pop(len(t)-1)
                else:
                    return False
        return not bool(t)


if __name__ == '__main__':
    s = Solution()
    s.isValid('{[]}')
