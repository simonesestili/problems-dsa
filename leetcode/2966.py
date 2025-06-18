class Solution:
    def divideArray(self, nums, k):
        ans, nums = [], sorted(nums)
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            ans.append(nums[i:i+3])
        return ans
