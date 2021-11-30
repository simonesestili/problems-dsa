class Solution:
    def combinationSum3(self, k, n):
        self.combs = []

        def dfs(curr, curr_sum):
            if len(curr) == k and curr_sum == n:
                self.combs.append(curr[:])
                return
            for i in range(1 if not curr else curr[-1] + 1, 10):
                if i not in curr:
                    curr.append(i)
                    dfs(curr, curr_sum + i)
                    curr.pop()

        dfs([], 0)
        return self.combs
