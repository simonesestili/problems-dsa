class Solution:
    def maximumANDSum(self, nums, slots):
        @cache
        def dp(i, mask):
            if i == len(nums): return 0
            best = 0
            for j in range(slots * 2):
                if (mask >> j) & 1:
                    slot_num = j // 2 + 1
                    best = max(best, (nums[i] & slot_num) + dp(i + 1, mask - (1 << j)))
            return best

        return dp(0, (1 << slots * 2) - 1)

