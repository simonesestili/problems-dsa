class Solution:
    def shipWithinDays(self, weights, days):

        def count(cap):
            res = curr = 0
            for w in weights:
                curr += w
                if curr > cap:
                    res += 1
                    curr = w
            return res + 1


        lo, hi = max(weights), sum(weights)
        while lo < hi:
            cand = (lo + hi) >> 1
            if count(cand) > days: lo = cand + 1
            else: hi = cand
        return lo
