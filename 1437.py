class Solution:
    def kLengthApart(self, nums, k):
        prev = None
        for i, x in enumerate(nums):
            if not x: continue
            if prev is not None and i - prev - 1 < k:
                return False
            prev = i
        return True
