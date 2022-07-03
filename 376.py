class Solution:
    def wiggleMaxLength(self, nums):
        top = bot = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                top, bot = bot + 1, bot
            elif nums[i] < nums[i-1]:
                top, bot = top, top + 1
        return max(top, bot)
