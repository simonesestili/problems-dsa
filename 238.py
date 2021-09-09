class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		product_left, product_right = [1] * n, [1] * n
		curr_left, curr_right = 1, 1
		for i in range(n):
			product_left[i], product_right[n - 1 - i] = curr_left, curr_right
			curr_left *= nums[i]
			curr_right *= nums[n - 1 - i]
		return [a * b for a, b in zip(product_left, product_right)]
