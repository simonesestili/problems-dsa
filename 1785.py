class Solution:
    def minElements(self, nums, limit, goal):
        return ceil(abs(goal - sum(nums)) / limit)
