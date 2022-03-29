class Solution:
    def findDuplicate(self, nums):
        lo, hi = 1, len(nums)
        while lo < hi:
            mid = (lo + hi) >> 1
            less = more = 0
            for x in nums:
                less += x <= mid
                more += x > mid
            if less > mid: hi = mid
            else: lo = mid + 1
        return lo
