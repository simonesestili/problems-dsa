class Solution:
    def subarrayLCM(self, nums, k):
        n, ans = len(nums), 0
        for i in range(n):
            curr = nums[i]
            for j in range(i, n):
                curr = math.lcm(curr, nums[j])
                if curr == k: ans += 1
        return ans
