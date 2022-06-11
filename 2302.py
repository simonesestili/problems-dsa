class Solution:
    def countSubarrays(self, nums, k):
        n, prefix = len(nums), list(accumulate(nums))
        ans = 0

        for i, x in enumerate(nums):
            if x >= k: continue
            lo, hi = i, n - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                val = (prefix[mid] - (0 if not i else prefix[i-1])) * (mid - i + 1)
                if val >= k: hi = mid - 1
                else: lo = mid
            ans += lo - i + 1

        return ans


