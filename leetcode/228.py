class Solution:
    def summaryRanges(self, nums):
        ans, i, n = [], 0, len(nums)
        nums.append(float('inf'))

        while i < n:
            prev = nums[i]
            while i < n and nums[i+1] == nums[i] + 1:
                i += 1
            if nums[i] == prev:
                ans.append(str(prev))
            else:
                ans.append(f'{prev}->{nums[i]}')
            i += 1

        return ans
