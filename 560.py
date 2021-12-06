class Solution:
    def subarraySum(self, nums, k):
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = curr = 0
        for num in nums:
            curr += num
            ans += prefix[curr - k]
            prefix[curr] += 1
        return ans

