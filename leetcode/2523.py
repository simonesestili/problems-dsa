class Solution:
    def closestPrimes(self, left, right):
        sieve = [True] * (right + 1)
        sieve[1] = False
        for i in range(2, int(sqrt(right)) + 1):
            if not sieve[i]: continue
            for p in range(i * i, right + 1, i):
                sieve[p] = False

        ans = prev = None
        for x in range(left, right + 1):
            if not sieve[x]: continue
            if prev and (not ans or ans[1] - ans[0] > x - prev):
                ans = [prev, x]
            prev = x
        return ans or [-1, -1]
