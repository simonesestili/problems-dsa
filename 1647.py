class Solution:
    def minDeletions(self, s):
        ans, curr = 0, float('inf')
        for v in sorted(Counter(s).values(), reverse=1):
            curr = max(min(v, curr - 1), 0)
            ans += v - curr
        return ans
