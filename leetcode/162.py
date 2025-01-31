class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            left = float('-inf') if not mid else nums[mid - 1]
            right = float('-inf') if mid + 1 == n else nums[mid + 1]
            if nums[mid] > left and nums[mid] > right:
                return mid
            if left > right:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo
