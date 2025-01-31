class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        nums.append(0)
        count = curr = prev = 0
        for x in nums:
            if x != prev: count, prev, curr = max(count, curr), x, 1
            else: curr += 1
        return count * k < len(nums)
