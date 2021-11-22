class Solution:
    def numOfWays(self, n):
        MOD = 10 ** 9 + 7
        diff = alternate = 6
        for _ in range(n - 1):
            diff, alternate = (diff * 2 + alternate * 2) % MOD, (diff * 2 + alternate * 3) % MOD
        return (diff + alternate) % MOD
