# O(n logn) solution with patience sort
class Solution:
    def lengthOfLIS(self, nums):
        piles = []
        for num in nums:
            idx = bisect_left(piles, num)
            if idx == len(piles):
                piles.append(num)
            else:
                piles[idx] = num
        return len(piles)        

# O(n^2) solution
# class Solution:     
# 	def lengthOfLIS(self, nums: List[int]) -> int:
#         subproblems = [1] * len(nums)
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     subproblems[i] = max(subproblems[i], subproblems[j] + 1)
#         return max(subproblems)
