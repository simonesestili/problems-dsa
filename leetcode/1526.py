class Solution:
    def minNumberOperations(self, target):
        ans = prev = 0
        for x in target:
            ans += max(x - prev, 0)
            prev = x
        return ans
