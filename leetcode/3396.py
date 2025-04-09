class Solution:
    def minimumOperations(self, nums):
        n, seen = len(nums), set()
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                return (i + 3) // 3
            seen.add(nums[i])
        return 0
