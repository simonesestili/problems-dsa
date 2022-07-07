class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False

        @cache
        def dp(i, j):
            if i == m: return s3[j-n:] == s2[j-n:]
            if j == n: return s3[i-m:] == s1[i-m:]
            if s3[i+j] == s1[i] and dp(i + 1, j):
                return True
            if s3[i+j] == s2[j] and dp(i, j + 1):
                return True

        return dp(0, 0)
