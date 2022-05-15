class Solution:
    def findMaxForm(self, strs, m, n):
        k = len(strs)
        counters = [[0] * 2 for _ in range(k)]

        for i, s in enumerate(strs):
            for c in map(int, s):
                counters[i][c] += 1

        @cache
        def dp(i, z, o):
            if i == k: return 0

            best = dp(i + 1, z, o)
            zeros, ones = counters[i]
            if zeros <= z and ones <= o:
                cand = 1 + dp(i + 1, z - zeros, o - ones)
                best = max(best, cand)

            return best

        return dp(0, m, n)


