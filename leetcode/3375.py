class Solution:
    def minOperations(self, nums, k):
        return len({x for x in nums if x > k}) if min(nums) >= k else -1
