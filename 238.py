class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
        prefix = suffix = 1
        ans = [1] * n
        for i in range(n):
            ans[i] *= prefix
            ans[n - 1 - i] *= suffix
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
        return ans
