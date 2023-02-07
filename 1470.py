class Solution:
    def shuffle(self, nums, n):
        ans = [0] * (2 * n)
        for i in range(0, 2 * n, 2):
            ans[i], ans[i+1] = nums[i//2], nums[i//2+n]
        return ans
