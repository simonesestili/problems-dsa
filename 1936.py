class Solution:
    def addRungs(self, rungs, dist):
        n, rungs = len(rungs) + 1, [0] + rungs

        ans = 0
        for i in range(n - 1):
            diff = rungs[i+1] - rungs[i]
            ans += (diff - 1) // dist

        return ans

