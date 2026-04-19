class Solution:
    def minMirrorPairDistance(self, nums):
        ans, seen = inf, {}
        for i, x in enumerate(nums):
            if x in seen:
                ans = min(ans, i - seen[x])
            seen[int(str(x)[::-1])] = i
        return -1 if ans == inf else ans
