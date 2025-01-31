class Solution:
    def executeInstructions(self, n, start, s):
        m = len(s)
        ans = [0] * m
        for i in range(m):
            r, c = start
            for j in range(i, m):
                if s[j] == 'U': r -= 1
                elif s[j] == 'D': r += 1
                elif s[j] == 'L': c -= 1
                elif s[j] == 'R': c += 1
                if r < 0 or c < 0 or r >= n or c >= n: break
                ans[i] += 1

        return ans
