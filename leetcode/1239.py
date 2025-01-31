class Solution:
    def maxLength(self, arr):
        code = lambda c: ord(c) - ord('a')
        def to_bitset(s, seen=0):
            for c in s:
                if seen >> code(c) & 1: return 0
                seen |= 1 << code(c)
            return seen

        arr = [to_bitset(s) for s in arr]
        @cache
        def dp(i, seen):
            if i == len(arr): return 0
            ans = dp(i + 1, seen)
            if not seen & arr[i]: ans = max(ans, dp(i + 1, seen | arr[i]) + arr[i].bit_count())
            return ans

        return dp(0, 0)
