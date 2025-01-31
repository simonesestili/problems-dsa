class Solution:
    def minOperations(self, nums, x):
        best, n, suffix = float('inf'), len(nums), 0
        prefix = {0: -1} | {val: i for i, val in enumerate(accumulate(nums))}

        for i in range(n - 1, -1, -1):
            suffix += nums[i]
            if x - suffix in prefix:
                if prefix[x - suffix] >= i: break
                best = min(best, prefix[x - suffix] + 1 + n - i)

        best = min(best, prefix.get(x, float('inf')) + 1)
        return -1 if best == float('inf') else best
