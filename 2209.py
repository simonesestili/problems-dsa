class Solution:
    def minimumWhiteTiles(self, floor, num, length):
        n = len(floor)

        @cache
        def dp(i, rem):
            if i >= n: return 0
            nocarpet = int(floor[i] == '1') + dp(i + 1, rem)
            carpet = float('inf') if rem == 0 else dp(i + length, rem - 1)
            return min(nocarpet, carpet)

        return dp(0, num)
