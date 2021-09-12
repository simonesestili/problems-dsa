class Solution:     
    def jump(self, nums: List[int]) -> int: 
        curr, furthest, end = 0, nums[0], len(nums) - 1
        jumps = 0

        while curr < end:
            jumps += 1
            if furthest >= end:
                return jumps
            for i in range(curr + 1, furthest + 1):
                if i + nums[i] > furthest:
                    curr, furthest = i, i + nums[i]

        return jumps
