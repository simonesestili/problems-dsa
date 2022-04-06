class Solution:
    def numDupDigitsAtMostN(self, n):
        uniques, m = 0, int(log10(n)) + 1
        dp, used = [0] * m, set()
        dp[-1], f = factorial(9) // factorial(10 - m), 9
        for i in range(m - 2, -1, -1):
            dp[i] = dp[i+1] // f
            f -= 1

        prod = curr = 9
        for _ in range(m - 1):
            uniques += prod
            prod *= curr
            curr -= 1

        for i, d in enumerate(map(int, str(n))):
            for cand in range(len(used) == 0, d):
                if cand in used: continue
                uniques += dp[m - 1 - i]
            if d in used: return n - uniques
            used.add(d)

        return n - uniques - 1
