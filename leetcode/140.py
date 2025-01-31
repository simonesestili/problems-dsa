class Solution:
    def wordBreak(self, s, words):
        n, words = len(s), set(words)

        ans, curr = [], []
        def dfs(i):
            if i == n:
                ans.append(' '.join(curr))
                return
            for j in range(i, n):
                if s[i:j+1] not in words: continue
                curr.append(s[i:j+1])
                dfs(j+1)
                curr.pop()

        dfs(0)
        return ans
