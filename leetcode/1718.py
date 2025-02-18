class Solution:
    def constructDistancedSequence(self, n):
        ans, used = [0] * (2 * n - 1), set()

        def dfs(i):
            if i == len(ans):
                return len(used) == n
            if ans[i]:
                return dfs(i+1)

            for x in range(n, 0, -1):
                if x not in used and (x == 1 or i+x < len(ans) and not ans[i+x]):
                    ans[i] = x
                    if x > 1: ans[i+x] = x
                    used.add(x)
                    if dfs(i+1):
                        return True
                    ans[i] = 0
                    if x > 1: ans[i+x] = 0
                    used.remove(x)

            return False

        dfs(0)
        return ans
