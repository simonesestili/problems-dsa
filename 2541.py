class Solution:
    def minOperations(self, nums1, nums2, k):
        if k == 0:
            return -1 if any(a != b for a, b in zip(nums1, nums2)) else 0

        inc = dec = 0
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            if d % k: return -1
            if a - b > 0: inc += d // k
            else: dec += d // k
        return -1 if inc != dec else inc


