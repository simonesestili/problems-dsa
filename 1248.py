class Solution:
    def numberOfSubarrays(self, nums, k):
        ans, curr, prefix = 0, 0, defaultdict(int)
        prefix[0] = 1
        for x in nums:
            curr += x % 2
            ans += prefix[curr - k]
            prefix[curr] += 1
        return ans

