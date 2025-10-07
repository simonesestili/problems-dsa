class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans, full, drys = [-1] * n, {}, SortedList()

        for i, r in enumerate(rains):
            if r == 0:
                drys.add(i)
                continue
            if r in full:
                idx = drys.bisect_right(full[r])
                if idx >= len(drys):
                    return []
                ans[drys.pop(idx)] = r
            full[r] = i

        while drys:
            ans[drys.pop()] = 1

        return ans
