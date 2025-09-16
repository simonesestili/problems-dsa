class Solution:
    def replaceNonCoprimes(self, nums):
        ans = []
        for x in nums:
            ans.append(x)
            while len(ans) > 1 and (g := gcd(ans[-2], ans[-1])) > 1:
                ans.append(ans.pop() * ans.pop() // g)
        return ans
