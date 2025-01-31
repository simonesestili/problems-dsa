class Solution:
    def merge(self, nums1, m, nums2, n):
        m, n = m - 1, n - 1
        for i in range(m + n + 1, -1, -1):
            if n < 0 or nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1

        for i in range(n, -1, -1):
            nums1[i] = nums2[i]
