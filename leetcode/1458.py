class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        @cache
        def dp(i=0, j=0, empty=True):
            if i >= n or j >= m: return float('-inf') if empty else 0
            first = nums1[i] * nums2[j] + dp(i + 1, j + 1, False)
            second = dp(i + 1, j, empty)
            third = dp(i, j + 1, empty)
            return max(first, second, third)

        return dp()
