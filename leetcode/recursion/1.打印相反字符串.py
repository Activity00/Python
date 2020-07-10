

class Solution:
    def printReverse(self, chars):
        if len(chars) == 1:
            return
        self.printReverse(chars[1:])
        print(chars[0])


if __name__ == '__main__':
    s = Solution()
    s.printReverse('abcdefg')
