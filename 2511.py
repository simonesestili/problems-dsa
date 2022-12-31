class Solution:
    def captureForts(self, forts):
        ans = 0
        seen = -1
        for i, x in enumerate(forts):
            if x:
                if seen >= 0 and forts[seen] == -x:
                    ans = max(ans, i - seen - 1)
                seen = i
        return ans
