class Solution:
    def zeroFilledSubarray(self, nums):
        ans = curr = 0
        for x in nums:
            curr = curr + 1 if x == 0 else 0
            ans += curr
        return ans
