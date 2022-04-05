class Solution:
    def longestConsecutive(self, nums):
        ans, nums = 0, set(nums)

        for num in nums:
            if num - 1 in nums: continue
            last = num + 1
            while last in nums: last += 1
            ans = max(ans, last - num)

        return ans

