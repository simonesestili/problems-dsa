class Solution:
    def largestVariance(self, s):

        def solve(a, b, vals):
            bseen = False
            ans = curr = float('-inf')
            for x in vals:
                if x > curr + x: bseen = False
                bseen |= x == -1
                curr = max(x, curr + x)
                ans = max(ans, curr - (not bseen))
            return ans

        best, letters = 0, set(s)
        for i in letters:
            for j in letters:
                if i == j: continue
                vals = [1 if c == i else -1 for c in s if c in {i, j}]
                cand = solve(i, j, vals)
                best = max(best, cand)

        return best
