class Solution:
    def rearrangeArray(self, nums):
        n, nums = len(nums), sorted(nums)
        ans, left, right = [], 0, n - 1

        while left <= right:
            ans.append(nums[left])
            left += 1
            if left <= right:
                ans.append(nums[right])
                right -= 1

        return ans
