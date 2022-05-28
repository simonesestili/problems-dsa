class Solution:
    def findMaxForm(self, strs, m, n):
        k = len(strs)
        counts = lambda s: (s.count('0'), s.count('1'))
        counters = list(map(counts, strs))

        @cache
        def dp(i, z, o):
            if i == k: return 0
            zeros, ones = counters[i]

            skip = dp(i + 1, z, o) # Dont pick ith string
            if zeros > z or ones > o: # We must skip ith string
                return skip

            pick = 1 + dp(i + 1, z - zeros, o - ones) # Pick ith string
            return max(skip, pick)

        return dp(0, m, n)
