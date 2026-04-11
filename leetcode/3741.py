class Solution:
    def minimumDistance(self, nums):
        ans, vals = inf, defaultdict(list)
        for i, x in enumerate(nums):
            vals[x].append(i)
            if len(vals[x]) >= 3:
                ans = min(ans, 2 * (vals[x][-1] - vals[x][-3]))
        return -1 if ans == inf else ans
