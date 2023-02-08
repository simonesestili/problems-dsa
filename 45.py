class Solution:     
    def jump(self, nums):
        jumps = curr = 0
        furthest = nums[0]

        while curr < len(nums) - 1:
            jumps += 1
            if furthest >= len(nums) - 1:
                break
            for i in range(curr + 1, min(furthest + 1, len(nums))):
                if i + nums[i] > furthest:
                    curr, furthest = i, i + nums[i]

        return jumps
