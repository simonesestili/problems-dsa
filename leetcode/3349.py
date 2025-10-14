class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        i, j = 0, k
        while j + k <= len(nums):
            for _ in range(k - 1):
                i, j = i + 1, j + 1
                if nums[i-1] >= nums[i] or nums[j-1] >= nums[j]:
                    break
            else:
                return True
        return False
