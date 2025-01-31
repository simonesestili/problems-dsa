class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
        maximum, curr = float('-inf'), float('-inf')
        for x in nums:
            curr = max(x, curr + x)
            maximum = max(maximum, curr)
        return maximum
