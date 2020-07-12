class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        if K % 2 == 0:
            return 1 if self.kthGrammar(N - 1, K//2) == 0 else 0
        else:
            return 0 if self.kthGrammar(N - 1, (K+1)//2) == 0 else 1


if __name__ == '__main__':
    s = Solution()
    print(s.kthGrammar(4, 5))
