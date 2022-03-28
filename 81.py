class Solution:
    def search(self, nums, target):

        def value(start, i):
            if nums[start] <= target:
                return nums[i] if nums[i] >= nums[start] else float('inf')
            return nums[i] if nums[i] < nums[start] else float('-inf')

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[lo] == nums[hi]: lo += 1
            elif value(lo, mid) < target: lo = mid + 1
            else: hi = mid
        return nums[lo] == target
