class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = suffix = 1
        ans = [1] * n
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]
            ans[n - 1 - i] *= suffix
            suffix *= nums[n - 1 - i]
        return ans