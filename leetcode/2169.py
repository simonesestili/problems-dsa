class Solution:
    def countOperations(self, a, b):
        ans = 0
        a, b = sorted((a, b))
        while a:
            d, r = divmod(b, a)
            a, b = r, a
            ans += d
        return ans
