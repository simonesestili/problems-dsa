class Solution:
    def xorAllNums(self, a, b):
        ans = 0
        if len(b) & 1:
            for x in a:
                ans ^= x
        if len(a) & 1:
            for x in b:
                ans ^= x
        return ans
