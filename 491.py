class Solution:
    def findSubsequences(self, nums):
        subs = set()

        def dfs(prev, i, curr):
            if i == len(nums):
                if len(curr) > 1: subs.add(tuple(curr))
                return

            if prev <= nums[i]:
                dfs(nums[i], i + 1, curr + [nums[i]])
            dfs(prev, i + 1, curr)

        dfs(float('-inf'), 0, [])
        return subs
