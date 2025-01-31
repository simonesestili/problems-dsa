class Solution:     
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        max_prefix, min_suffix = [float('-inf')], [float('inf')]

        for i in range(n):
            max_prefix.append(max(max_prefix[-1], nums[i]))
            min_suffix.append(min(min_suffix[-1], nums[-1-i]))
        min_suffix = min_suffix[::-1]

        left, right = 0, n - 1
        while left < n - 1 and max_prefix[left+1] <= min_suffix[left+1]:
            left += 1
        while right > 0 and min_suffix[right] >= max_prefix[right]:
            right -= 1
        
        size = right - left + 1
        return 0 if size <= 1 else size
