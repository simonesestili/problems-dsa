class Solution:
    def minOperations(self, nums):
        ans, prev = 0, float('-inf')

        for x in nums:
            if x < prev:
                ans += prev - x + 1
                prev = x + 1
            else:
                prev = x

        return ans
