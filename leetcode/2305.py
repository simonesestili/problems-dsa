class Solution:
    def distributeCookies(self, cookies, k):
        n, sums = len(cookies), []
        for mask in range(1 << n):
            sums.append(sum(cookies[i] for i in range(n) if mask >> i & 1))

        @cache
        def dp(mask, rem):
            if mask == 0 or rem < 0: return float('inf') if rem else 0
            ans = float('inf')
            for submask in range(1 << n):
                if mask & submask != submask: continue
                ans = min(ans, max(sums[submask], dp(mask - submask, rem - 1)))
            return ans

        return dp((1 << n) - 1, k)
