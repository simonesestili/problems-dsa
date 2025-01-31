class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        for i in range(len(nums)):
            if start - i >= 0 and nums[start - i] == target:
                return i
            if start + i < len(nums) and nums[start + i] == target:
                return i
        return None
