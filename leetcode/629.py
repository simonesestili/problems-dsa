MOD = 10 ** 9 + 7
class Solution:
    def kInversePairs(self, n, k):
        prefix = [1] * (k + 1)

        for size in range(2, n + 1):
            nxt = []
            for inv in range(k + 1):
                nxt.append(nxt[-1] if nxt else 0)
                nxt[-1] += prefix[inv] - (0 if inv < size else prefix[inv-size])
                nxt[-1] %= MOD
            prefix = nxt

        return prefix[k] if not k else (prefix[k] - prefix[k-1]) % MOD
