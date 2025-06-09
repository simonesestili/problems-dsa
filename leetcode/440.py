class Solution:
    def findKthNumber(self, n, k):
        ans, k = 1, k - 1

        while k:
            cnt = 0
            vals = [ans, ans+1]
            while vals[0] <= n:
                cnt += min(n + 1, vals[1]) - vals[0]
                vals = [vals[0] * 10, vals[1] * 10]

            if cnt <= k:
                ans += 1
                k -= cnt
            else:
                ans *= 10
                k -= 1

        return ans
