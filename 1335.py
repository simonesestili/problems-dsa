class Solution:
    def minDifficulty(self, jobs, days):
        n = len(jobs)
        if days > n: return -1

        @cache
        def dp(i, rem):
            if i == n: return 0
            if not rem: return float('inf')
            ans, curr = float('inf'), 0
            for j in range(i, n - rem + 1):
                curr = max(curr, jobs[j])
                ans = min(ans, curr + dp(j + 1, rem - 1))
            return ans

        return dp(0, days)
