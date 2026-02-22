class Solution:
    def binaryGap(self, n):
        ans = curr = prev = 0
        while n:
            curr += 1
            if n & 1:
                if prev:
                    ans = max(ans, curr - prev)
                prev = curr
            n >>= 1
        return ans
