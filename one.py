class Solution:
    def areNumbersAscending(s):
        # Extract the tokens which are numbers
        nums = [num for num in s.split() if num.isnumeric()]
        # Make sure that each adjacent pair is increasing, if not return false
        for i in range(len(nums) - 1):
            if int(nums[i]) >= int(nums[i + 1]):
                return False
        # Since all adjacent pairs are increasing return true    
        return True    
