class Solution:
    def solve(self, nums):
        n = len(nums)
        ans, suffix = [0] * n, [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        curr = 1
        for i in range(n):
            ans[i] = curr * suffix[i]
            curr *= nums[i]
        return ans
