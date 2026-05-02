class Solution:
    def minOperations(self, grid, x):
        nums, rem = [], grid[0][0] % x
        for row in grid:
            for val in row:
                if val % x != rem:
                    return -1
                nums.append(val)
        nums.sort()
        med = nums[len(nums)//2]
        return sum(abs(med-val) // x for val in nums)
