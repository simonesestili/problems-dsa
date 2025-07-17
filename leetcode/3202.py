class Solution:
    def maximumLength(self, nums, k):
        ans, nums = 0, [num % k for num in nums]
        for x in range(k):
            seen = defaultdict(int)
            for num in nums:
                seen[num] = max(seen[num], seen[(x - num) % k] + 1)
                ans = max(ans, seen[num])
        return ans
