class Solution:
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        best, curr, seen = 0, 0, {}
        left = 0
        for right in range(n):
            while nums[right] in seen:
                curr -= nums[left]
                del seen[nums[left]]
                left += 1
            curr += nums[right]
            seen[nums[right]] = right
            best = max(best, curr)
        return best
