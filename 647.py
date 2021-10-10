class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        substrs = [[False] * n for _ in range(n)]

        def fill(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                substrs[left][right] = True
                left -= 1
                right += 1

        for i in range(n):
            fill(i, i)
            fill(i, i + 1)
            
        count = 0
        for i in range(n):
            for j in range(n):
                count += substrs[i][j]
        return count
