MOD = 10 ** 9 + 7
class Solution:
    def countVowelPermutation(self, n):
        a = e = i = o = u = 1
        for _ in range(n - 1):
            A = (e + i + u) % MOD
            E = (a + i) % MOD
            I = (e + o) % MOD
            O = (i) % MOD
            U = (i + o) % MOD
            a, e, i, o, u = A, E, I, O, U
        return sum((a, e, i, o, u)) % MOD
