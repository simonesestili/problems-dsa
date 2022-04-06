class Solution:
    def findLength(self, a, b):
        m, n = len(a), len(b)

        lo, hi = 0, min(m, n)
        while lo < hi:
            length = (lo + hi + 1) // 2
            if self.hashes(a, length) & self.hashes(b, length):
                lo = length
            else:
                hi = length - 1

        return lo

    def hashes(self, arr, length):
        BASE, MOD = 101, pow(10, 9) + 7
        REM = pow(BASE, length - 1, MOD)
        curr, seen = 0, set()

        for i in range(length - 1):
            curr = (curr * BASE + arr[i]) % MOD

        left = 0
        for right in range(length - 1, len(arr)):
            curr = (curr * BASE + arr[right]) % MOD
            seen.add(curr)
            curr = (curr - arr[left] * REM) % MOD
            left += 1

        return seen
