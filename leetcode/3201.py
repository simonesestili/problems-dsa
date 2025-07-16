class Solution:
    def maximumLength(self, nums):
        zeros = ones = alt = 0
        prev = nums[0] & 1 ^ 1
        for x in nums:
            zeros += x % 2 == 0
            ones += x % 2 == 1
            if x % 2 != prev:
                prev ^= 1
                alt += 1
        return max(zeros, ones, alt)
