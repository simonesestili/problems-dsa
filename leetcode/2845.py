class Solution:
    def countInterestingSubarrays(self, nums, mod, k):
        ans, curr, seen = 0, 0, defaultdict(int, {0: 1})
        for x in nums:
            curr = (curr + int(x % mod == k)) % mod
            ans += seen[(curr - k) % mod]
            seen[curr] += 1
        return ans
