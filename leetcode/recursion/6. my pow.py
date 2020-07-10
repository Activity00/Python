import sys
sys.setrecursionlimit(1000) #例如这里设置为十万


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(1.00001, 123456))

