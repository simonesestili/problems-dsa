from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums):
        seen = SortedList()
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            nums[i] = seen.bisect_left(x)
            seen.add(x)
        return nums
