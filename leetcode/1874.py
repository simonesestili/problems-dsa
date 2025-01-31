class Solution:
    def minProductSum(self, nums1, nums2):
        return sum(a * b for a, b in zip(sorted(nums1), sorted(nums2, reverse=True)))
