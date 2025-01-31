class Solution:
    def findMaxLength(self, nums):
        ans = curr = 0
        seen = {0: -1}

        for i, x in enumerate(nums):
            curr += 1 if x else -1
            if curr in seen: ans = max(ans, i - seen[curr])
            else: seen[curr] = i

        return ans
