class Solution:
    def minSum(self, nums1, nums2):
        mn1, inc1 = sum(x or 1 for x in nums1), any(x == 0 for x in nums1)
        mn2, inc2 = sum(x or 1 for x in nums2), any(x == 0 for x in nums2)
        return -1 if mn1 < mn2 and not inc1 or mn2 < mn1 and not inc2 else max(mn1, mn2)
