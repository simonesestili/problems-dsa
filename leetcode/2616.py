class Solution:
    def minimizeMax(self, nums, p):
        nums.sort()

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            cand = (lo + hi) // 2
            i, cnt = 1, 0
            while i < len(nums):
                if nums[i] - nums[i - 1] <= cand:
                    cnt += 1
                    i += 1
                i += 1
            if cnt >= p: hi = cand
            else: lo = cand + 1

        return lo
