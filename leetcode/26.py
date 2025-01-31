class Solution:
    def removeDuplicates(self, nums):
        n, fast = len(nums), 0
        for slow in range(n):
            if fast >= n: return slow
            nums[slow] = nums[fast]
            while fast < n and nums[fast] == nums[slow]: fast += 1
        return n
