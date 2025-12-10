MOD = 10 ** 9 + 7
class Solution:
    def specialTriplets(self, nums):
        ans, lcnts, rcnts = 0, Counter(), Counter(nums)
        for x in nums:
            rcnts[x] -= 1
            ans = (ans + lcnts[x*2] * rcnts[x*2]) % MOD
            lcnts[x] += 1
        return ans
