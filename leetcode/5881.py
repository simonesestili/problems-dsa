class Solution:     
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)         
        currMax = nums[0]         
        maxes = [0] * n         
        maximum = -1
        for i in range(n):
            maximum = max(maximum, maxes[i] - nums[i])
        return -1 if maximum <= 0 else maximum
