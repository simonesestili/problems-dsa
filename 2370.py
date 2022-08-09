class Solution:
    def longestIdealString(self, s, k):
        ans, seen = 1, defaultdict(int)
        for x in map(ord, s):
            cand = 1 + max(seen[c] for c in range(x - k, x + k + 1))
            seen[x] = max(seen[x], cand)
            ans = max(ans, cand)
        return ans
