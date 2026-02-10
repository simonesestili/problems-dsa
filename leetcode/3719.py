class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt, seen = 0, set()
            for j in range(i, n):
                if nums[j] not in seen:
                    cnt += 1 if nums[j] % 2 else -1
                    seen.add(nums[j])
                if cnt == 0:
                    ans = max(ans, j - i + 1)
        return ans
