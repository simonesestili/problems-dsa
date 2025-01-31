class Solution:
    def countBadPairs(self, nums):
        n, valid = len(nums), 0
        seen = defaultdict(int)
        for i, x in enumerate(nums):
            valid += seen[i - x]
            seen[i - x] += 1
        return n * (n - 1) // 2 - valid
