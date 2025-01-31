class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)

        def length(val):
            last = val + 1
            while last in nums: last += 1
            return last - val

        return max((length(num) for num in nums if num - 1 not in nums), default=0)
