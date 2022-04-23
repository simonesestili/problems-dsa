class Solution:
    def minDeletions(self, s):
        n, freqs = len(s), sorted(Counter(s).values(), reverse=1)

        ans, curr = 0, float('inf')
        for v in freqs:
            if v < curr:
                curr = v
            else:
                curr -= 1
                ans += v - curr

        return ans
