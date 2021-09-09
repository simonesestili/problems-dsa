class NumArray:      
	def __init__(self, nums: List[int]):       
		self.total = sum(nums)
		self.total_right = [0] * len(nums)
		self.total_left = [0] * len(nums)
		curr_right, curr_left = 0, 0
		for i in range(len(nums)):
			self.total_left[i] = curr_left
			curr_left += nums[i]
			self.total_right[len(nums) - 1 - i] = curr_right
			curr_right += nums[len(nums) - 1 - i]	

	def sumRange(self, left: int, right: int) -> int:
		return self.total - self.total_left[left] - self.total_right[right]	
