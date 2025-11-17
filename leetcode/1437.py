class Solution:
    def kLengthApart(self, nums, k):
        prev = -inf
        for i, x in enumerate(nums):
            if x and i - prev - 1 < k:
                return False
            elif x:
                prev = i
        return True
