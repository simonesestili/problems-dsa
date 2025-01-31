class Solution:
    def zeroFilledSubarray(self, nums):
        total, curr, prev = 0, 0, False
        for x in nums:
            if x:
                curr, prev = 0, False
            else:
                curr, prev = curr + 1, True
            total += curr
        return total
