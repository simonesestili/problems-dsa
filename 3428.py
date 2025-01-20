MOD = 10**9 + 7

fact = [1]
inv = [1]
for i in range(1, 10**5):
    fact.append(i * fact[-1] % MOD)
    inv.append(pow(fact[-1], -1, MOD))

combs = [[0] * 100 for _ in range(10**5)]
for n in range(10**5):
    for r in range(100):
        combs[n][r] = fact[n] * inv[r] * inv[n-r] % MOD

class Solution:
    def minMaxSums(self, nums, k):
        n, nums = len(nums), sorted(nums)

        ans = 0
        for i, x in enumerate(nums):
            for r in range(k):
                left = combs[i][r] if i >= r else 0
                right = combs[n - i - 1][r] if n - i - 1 >= r else 0
                ans = (ans + x * (left + right)) % MOD

        return ans
