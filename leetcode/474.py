class Solution:
    def findMaxForm(self, strs, m, n):
        cnts = [(s.count('0'), s.count('1')) for s in strs]

        @cache
        def dp(i, z, o):
            if i == len(strs):
                return 0
            skip = dp(i + 1, z, o)
            pick = 1 + dp(i + 1, z - cnts[i][0], o - cnts[i][1]) if min(z - cnts[i][0], o - cnts[i][1]) >= 0 else 0
            return max(skip, pick)

        return dp(0, m, n)
