class Solution:
    def minCapability(self, nums, k):
        def valid(cap):
            curr = i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    curr += 1
                    i += 1
                i += 1
            return curr >= k

        lo, hi = min(nums), max(nums)
        while lo < hi:
            cand = (lo + hi) // 2
            if valid(cand): hi = cand
            else: lo = cand + 1
        return lo
