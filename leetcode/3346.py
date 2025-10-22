class Solution:
    def maxFrequency(self, nums, k, ops):
        cnts = Counter(nums)
        nums = sorted(nums)
        ans = 0
        for i, x in enumerate(nums):
            a = min(bisect_right(nums, x + k) - bisect_left(nums, x - k) - cnts[x], ops) + cnts[x]
            b = min(bisect_right(nums, x + 2 * k) - i, ops)
            ans = max(ans, a, b)
        return ans
