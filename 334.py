class Solution:
    def increasingTriplet(self, nums):
        left = mid = float('inf')
        for x in nums:
            if x > mid: return True
            if x > left: mid = x
            else: left = x
        return False
