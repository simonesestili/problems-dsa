class Solution:
	def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        nums.append(right + 1)
        total = length = consec_length = to_remove = 0
        for num in nums:
            if num > right:
                total += (length * (length + 1) // 2) - (consec_length * (consec_length + 1) // 2 + to_remove)
                length = consec_length = to_remove = 0
            elif num >= left:
                length += 1
                if consec_length:
                    to_remove += consec_length * (consec_length + 1) // 2
                    consec_length = 0
            else:
                length += 1
                consec_length += 1
        return total
