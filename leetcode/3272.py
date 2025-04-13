class Solution:
    def countGoodIntegers(self, n, k):
        ans, seen = 0, set()
        for half in range(pow(10, (n + 1) // 2 - 1), pow(10, (n + 1) // 2)):
            cand = str(half) + str(half)[::-1][n % 2:]
            digits = tuple(sorted(cand))
            if int(cand) % k == 0 and digits not in seen:
                seen.add(digits)
                cnts = Counter(digits)
                contrib = (n - cnts['0']) * factorial(n - 1)
                for cnt in cnts.values():
                    contrib //= factorial(cnt)
                ans += contrib
        return ans
