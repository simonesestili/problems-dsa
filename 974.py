class Solution:
    def subarraysDivByK(self, nums, k):
        ans = curr = 0
        seen = defaultdict(int); seen[0] = 1
        for x in nums:
            curr = (curr + x) % k
            ans += seen[curr]
            seen[curr] += 1
        return ans
