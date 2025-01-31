class Solution:
    def numSquarefulPerms(self, nums):
        n, nums = len(nums), sorted(nums)

        @cache
        def dp(mask, prev):
            if not mask: return 1
            count, seen = 0, set()
            for i in range(n):
                if not mask & (1 << i): continue
                if nums[i] not in seen and self.squareful(prev, nums[i]):
                    count += dp(mask - (1 << i), nums[i])
                    seen.add(nums[i])
            return count

        return dp((1 << n) - 1, -1)

    def squareful(self, p, c):
        return p == -1 or int(sqrt(p + c)) == sqrt(p + c)
