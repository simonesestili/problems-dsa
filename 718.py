BASE = 101
MOD = 10 ** 9 + 7
class Solution:
    def findLength(self, a, b):

        def hashed(arr, size):
            rem = pow(BASE, size - 1, MOD)
            curr, seen = 0, set()
            for i in range(size - 1): curr = (curr * BASE + arr[i]) % MOD
            for right in range(size - 1, len(arr)):
                left = right - size + 1
                curr = (curr * BASE + arr[right]) % MOD
                seen.add(curr)
                curr = (curr - rem * arr[left]) % MOD
            return seen

        lo, hi = 0, min(len(a), len(b))
        while lo < hi:
            cand = (lo + hi + 1) // 2
            if hashed(a, cand) & hashed(b, cand): lo = cand
            else: hi = cand - 1
        return lo
