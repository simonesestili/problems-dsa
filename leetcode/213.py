class Solution:     
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        prev, max1 = nums[0], max(nums[0], nums[1])
        for num in nums[2:-1]:
            prev, max1 = max1, max(max1, prev + num)
        prev, max2 = nums[1], max(nums[1], nums[2])
        for num in nums[3:]:
            prev, max2 = max2, max(max2, prev + num)
        return max(max1, max2)    
