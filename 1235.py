class Solution:
    def jobScheduling(self, starts, ends, profits):
        n, jobs, starts = len(starts), sorted(zip(starts, ends, profits)), sorted(starts)

        @cache
        def dp(i):
            if i == n: return 0
            nxt = bisect_left(jobs, (jobs[i][1], -inf, -inf))
            return max(jobs[i][2] + dp(nxt), dp(i + 1))

        return dp(0)
