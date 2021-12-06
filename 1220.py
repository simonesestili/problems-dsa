class Solution:
    def countVowelPermutation(self, n):
        M = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            A = (e + u + i) % M
            E = (a + i) % M
            I = (e + o) % M
            O = (i) % M
            U = (o + i) % M
            a, e, i, o, u = A, E, I, O, U

        return sum([a, e, i, o, u]) % M
