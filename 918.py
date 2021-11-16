class Solution:
    def maxSubarraySumCircular(self, nums):
        self.n = len(nums)
        prefix, suffix = self.prefix(nums), self.prefix(nums[::-1])[::-1]
        ans = best_prefix = float('-inf')
        for i in range(self.n):
            ans = max(ans, best_prefix + suffix[i])
            best_prefix = max(best_prefix, prefix[i])
        return max(ans, self.kadane(nums))

    def prefix(self, nums):
        A = [nums[0]] * self.n
        for i in range(1, self.n):
            A[i] = nums[i] + A[i - 1]
        return A

    def kadane(self, nums):
        best = prev = nums[0]
        for i in range(1, self.n):
            prev = max(nums[i], nums[i] + prev)
            best = max(best, prev)
        return best
