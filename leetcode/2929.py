class Solution:
    def distributeCandies(self, n, limit):
        ans = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2 * limit:
                ans += min(n - i, limit) - max(n - i - limit, 0) + 1
        return ans
