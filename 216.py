class Solution:
    def combinationSum3(self, k, n):
        self.combs, self.curr, = [], []

        def dfs(curr_sum=0):
            if len(self.curr) == k and curr_sum == n:
                self.combs.append(self.curr[:])
                return
            for i in range(1 if not self.curr else self.curr[-1] + 1, 10):
                if curr_sum + i > n: break
                self.curr.append(i)
                dfs(curr_sum + i)
                self.curr.pop()

        dfs()
        return self.combs
