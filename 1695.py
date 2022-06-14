class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        best = curr = left = 0

        for x in nums:
            curr += x
            while x in seen:
                seen.remove(nums[left])
                curr -= nums[left]
                left += 1
            seen.add(x)
            best = max(best, curr)

        return best
