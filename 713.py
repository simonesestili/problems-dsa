class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n, left = len(nums), 0
        
        ans, curr = 0, 1
        for right in range(n):
            curr *= nums[right]
            while curr >= k and left != right + 1:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans

