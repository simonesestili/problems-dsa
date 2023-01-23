class Solution:
    def getCommon(self, nums1, nums2):
        common = set(nums1) & set(nums2)
        return -1 if not common else min(common)
