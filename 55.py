class Solution:     
    def canJump(self, nums: List[int]) -> bool:
        curr, furthest = 0, nums[0]

        while True:
            if furthest >= len(nums) - 1:
                return True
            if nums[curr] == 0:
                return False
            for i in range(curr + 1, furthest + 1):
                if i + nums[i] >= furthest:
                    curr, furthest = i, i + nums[i]
