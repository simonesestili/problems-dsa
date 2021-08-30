class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		longest = 0
		used = -1
		curr = 0
		for i in range(len(nums)):
			if nums[i]:
				curr += 1
			else:
				curr = i - used
				used = i
			longest = max(longest, curr)
		return longest - 1
