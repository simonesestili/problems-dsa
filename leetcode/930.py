class Solution:
    def numSubarraysWithSum(self, nums, goal):
        ans = 0
        prefix, curr = {0: 1}, 0
        for x in nums:
            curr += x
            ans += prefix.get(curr - goal, 0)
            prefix[curr] = 1 + prefix.get(curr, 0)
        return ans
