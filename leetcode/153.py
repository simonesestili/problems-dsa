class Solution(object):     
	def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
