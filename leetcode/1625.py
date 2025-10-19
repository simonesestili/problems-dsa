class Solution:
    def findLexSmallestString(self, s, a, b):
        seen = set()
        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(s[b:] + s[:b])
            dfs(''.join(str((int(c)+a)%10) if i % 2 else c for i, c in enumerate(s)))
        dfs(s)
        return min(seen)
