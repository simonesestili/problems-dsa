class Solution:
    def specialArray(self, nums):
        n, nums = len(nums), sorted(nums)

        for x in range(1, n + 1):
            if nums[n-x] >= x and (x == n or nums[n-x-1] < x):
                return x

        return -1

