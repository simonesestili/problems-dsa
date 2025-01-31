class Solution:
    def smallestDistancePair(self, nums, k):
        n, nums = len(nums), sorted(nums)

        count = lambda d: sum(bisect_right(nums, nums[i] + d) - i - 1 for i in range(n))

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            cand = (lo + hi) // 2
            if count(cand) < k: lo = cand + 1
            else: hi = cand

        return lo
