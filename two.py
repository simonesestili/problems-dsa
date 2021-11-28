class Solution:
    def getAverages(self, nums, k):
        n, size = len(nums), 2 * k + 1
        ans = [-1] * n
        left, right, curr = 0, 2 * k, sum(nums[:size])
        while right < n:
            ans[(right + left) // 2] = curr // size
            curr -= nums[left]
            curr += 0 if right == n - 1 else nums[right + 1]
            left, right = left + 1, right + 1
        return ans
