class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)

        @cache
        def dp(i):
            if i == n: return 0
            ans = mx = arr[i]
            for j in range(i, min(i + k, n)):
                mx = max(mx, arr[j])
                ans = max(ans, mx * (j - i + 1) + dp(j + 1))
            return ans

        return dp(0)
