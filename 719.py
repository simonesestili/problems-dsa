class Solution:
    # time: O(n*log(n)*log(n))
    def smallestDistancePair(self, nums, k):
        n, nums = len(nums), sorted(nums)
        lo, hi = 0, nums[-1] - nums[0]

        count = lambda diff: sum(bisect_right(nums, nums[i] + diff) - i - 1 for i in range(n))

        while lo < hi:
            diff = (lo + hi) >> 1
            if count(diff) < k: lo = diff + 1
            else: hi = diff

        return lo
