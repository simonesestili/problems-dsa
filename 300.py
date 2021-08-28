class Solution:     
	def lengthOfLIS(self, nums: List[int]) -> int:
        subproblems = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    subproblems[i] = max(subproblems[i], subproblems[j] + 1)
        return max(subproblems)
