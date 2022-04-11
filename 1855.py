class Solution:
    def maxDistance(self, nums1, nums2):
        ans = 0
        m, n = len(nums1), len(nums2)

        def find(lo, hi, target):
            while lo < hi and (lo + hi + 1) >> 1 < n:
                mid = (lo + hi + 1) >> 1
                if nums2[mid] >= target:
                    lo = mid
                else:
                    hi = mid - 1
            return float('-inf') if lo >= n or nums2[lo] < target else lo


        for i in range(m):
            ans = max(ans, find(i + 1, n - 1, nums1[i]) - i)

        return ans

