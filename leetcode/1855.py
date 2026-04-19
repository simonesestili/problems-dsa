class Solution:
    def maxDistance(self, nums1, nums2):
        ans, i, n = 0, len(nums1) - 1, len(nums2)
        for j in range(n - 1, -1, -1):
            while i >= 0 and nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                i -= 1
        return ans
