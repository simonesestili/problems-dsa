class Solution:
    def checkSubarraySum(self, nums, k):
        prefix, curr = {0: -1}, 0
        for i, num in enumerate(nums):
            curr = (curr + num) % k
            if i - prefix.get(curr, i) >= 2:
                return True
            if curr % k not in prefix:
                prefix[curr % k] = i
        return False
