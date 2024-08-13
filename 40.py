class Solution:
    def combinationSum2(self, cands, target):
        cands.sort()
        dp = [{()}] + [set() for _ in range(target)]
        for i, x in enumerate(cands):
            if x > target: break
            for j in range(target, x - 1, -1):
                dp[j] |= {c + (x,) for c in dp[j - x]}

        return list(dp[target])

