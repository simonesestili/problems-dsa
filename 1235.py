class Solution:
    def jobScheduling(self, starts, ends, profits):
        n, jobs, starts = len(ends), sorted(list(zip(starts, ends, profits))), sorted(starts)

        @cache
        def dp(start):
            if start >= n: return 0
            i = bisect_left(starts, jobs[start][1])
            return max(jobs[start][2] + dp(i), dp(start + 1))

        return dp(0)
