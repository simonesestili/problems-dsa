class Solution:
    def splitArraySameAverage(self, nums):
        s, n = sum(nums), len(nums)

        @lru_cache(None)
        def find(target, k, i):
            if not target:
                return not k
            if target < 0 or i >= n:
                return False
            return find(target - nums[i], k - 1, i + 1) or find(target, k, i + 1)

        return any(not s * k % n and find(s * k // n, k, 0) for k in range(1, n // 2 + 1))
