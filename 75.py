class Solution:
    def sortColors(self, nums):
        red = white = blue = 0
        for col in nums:
            red += col == 0
            white += col == 1
            blue += col == 2
        white, blue, idx = white + red, red + white + blue, 0
        for i in range(len(nums)):
            nums[i] = 0 if i < red else 1 if i < white else 2
        return nums
