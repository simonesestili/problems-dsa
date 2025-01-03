class Solution:
    def maxCount(self, banned, n, mx):
        ans, curr, banned = 0, 0, set(banned)
        for x in range(1, n + 1):
            if x in banned: continue
            curr += x
            if curr > mx: break
            ans += 1
        return ans
