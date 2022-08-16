class Solution:
    def firstUniqChar(self, s):
        ans, seen = {}, set()
        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
                ans[c] = i
            elif c in ans: del ans[c]
        return -1 if not ans else min(ans.values())
