class Solution:
    def countValidSelections(self, nums):
        ans, left, right = 0, 0, sum(nums)
        for x in nums:
            left += x
            right -= x
            ans += 0 if x else int(abs(left - right) <= 1) + int(left == right)
        return ans
