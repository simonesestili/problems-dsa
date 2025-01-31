class Solution:     
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_ones = max_ones = 0
        for num in nums:
            if num:
                curr_ones += 1
            else:
                curr_ones = 0
            max_ones = max(max_ones, curr_ones)    
        return max_ones    
