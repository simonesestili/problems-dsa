class Solution:
    def sumScores(self, st):

        def z_function(s):
            n, l, r = len(s), 0, 0
            z = [0] * n
            for i in range(1, n):
                if i <= r: z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
                if i + z[i] - 1 > r: l, r = i, i + z[i] - 1
            return z

        return sum(z_function(st)) + len(st)
