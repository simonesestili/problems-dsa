class Solution:     
    def canJump(self, nums: List[int]) -> bool:
        left, furthest = 0, nums[0]

        while True:
            if furthest >= len(nums):
                return True
            elif not nums[left]:
                return False
            for i in range(left, furthest + 1):
                if i + nums[i] >= left + nums[left]:
                    left = i
            furthest = left + nums[left]
