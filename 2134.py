class Solution:
    def minSwaps(self, nums):
        n, cnt = len(nums), nums.count(1)
        ans = curr = nums[:cnt].count(0)
        for l in range(n):
            curr -= nums[l] == 0
            curr += nums[(l+cnt)%n] == 0
            ans = min(ans, curr)
        return ans

