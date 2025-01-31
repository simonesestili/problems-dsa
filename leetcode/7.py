class Solution:
    def reverse(self, x):
        ans, neg = 0, x < 0
        x = abs(x)
        while x:
            ans = ans * 10 + x % 10
            x //= 10
            if ans > (1 << 31) - 1: return 0
        return -ans if neg else ans
