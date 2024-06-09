class Solution:
    def subarraysDivByK(self, nums, k):
        ans = curr = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for x in nums:
            curr = (curr + x) % k
            ans += prefix[curr]
            prefix[curr] += 1
        return ans

