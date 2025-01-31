class Solution:
    def maxSubarraySumCircular(self, nums):
        total = 0
        mx = curr_mx = -inf
        mn = curr_mn = inf
        for x in nums:
            curr_mx = max(curr_mx + x, x)
            curr_mn = min(curr_mn + x, x)
            mx = max(mx, curr_mx)
            mn = min(mn, curr_mn)
            total += x
        return mx if total == mn else max(mx, total - mn)
