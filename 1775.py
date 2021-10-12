class Solution:
    def minOperations(self, nums1, nums2):
        counts1, counts2 = [0] * 7, [0] * 7
        for num in nums1:
            counts1[num] += 1
        for num in nums2:
            counts2[num] += 1
