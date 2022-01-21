class Solution:
    def combinationSum(self, cands, target):
        self.ans = []

        def dfs(curr, i, target):
            if target <= 0:
                if not target: self.ans.append(curr[:])
                return
            if i >= len(cands):
                return
            dfs(curr + [cands[i]], i, target - cands[i])
            dfs(curr[:], i + 1, target)

        dfs([], 0, target)
        return self.ans
