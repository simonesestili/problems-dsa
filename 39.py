class Solution:
    def combinationSum(self, cands, target):
        self.ans = []

        def dfs(curr, i, delta):
            if delta <= 0:
                if not delta: self.ans.append(curr[:])
                return
            if i >= len(cands):
                return
            dfs(curr + [cands[i]], i, delta - cands[i])
            dfs(curr, i + 1, delta)

        dfs([], 0, target)
        return self.ans
