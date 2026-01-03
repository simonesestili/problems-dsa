MOD = 10 ** 9 + 7
class Solution:
    def numOfWays(self, n):
        two = three = 6
        for _ in range(n - 1):
            two, three = (two * 2 + three * 2) % MOD, (two * 2 + three * 3) % MOD
        return (two + three) % MOD
