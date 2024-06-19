class Solution:
    def minDays(self, bloom, m, k):
        if len(bloom) < m * k: return -1
        lo, hi = 1, 10**9

        while lo < hi:
            cand = (lo + hi) // 2
            count = run = 0
            for x in bloom:
                if x <= cand: run += 1
                else: run = 0
                if run >= k:
                    count += 1
                    run = 0
            if count >= m:
                lo, hi = lo, cand
            else:
                lo, hi = cand + 1, hi

        return lo
