class Solution:
    def checkSubarraySum(self, nums, k):
        prefix, curr = {0: -1}, 0
        for i, x in enumerate(nums):
            curr = (curr + x) % k
            if i - prefix.get(curr, i) >= 2:
                return True
            if curr not in prefix:
                prefix[curr] = i
        return False

