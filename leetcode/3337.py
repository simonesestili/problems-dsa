MOD = 10**9+7

def matrix_multiply(a, b):
    ans = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ans[i][j] = (ans[i][j] + a[i][k] * b[k][j]) % MOD
    return ans

def matrix_pow(mat, p):
    n = len(mat)
    ans = [[int(i == j) for j in range(n)] for i in range(n)]
    while p:
        if p & 1:
            ans = matrix_multiply(ans, mat)
        mat = matrix_multiply(mat, mat)
        p >>= 1
    return ans

class Solution:
    def lengthAfterTransformations(self, s, t, nums):
        trans = [[0] * 26 for _ in range(26)]
        for c, cnt in enumerate(nums):
            for i in range(c + 1, c + cnt + 1):
                trans[c][i % 26] = 1
        trans = matrix_pow(trans, t)

        cnts = [0] * 26
        for c in s: cnts[ord(c) - ord('a')] += 1

        ans = matrix_multiply([cnts], trans)
        return sum(ans[0]) % MOD
