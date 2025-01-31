class Solution:
    def longestArithSeqLength(self, arr):
        n = len(arr)
        # dp[i][diff] = longest subsequence ending at index i with a difference of diff
        dp = [dict() for _ in range(n)]
        ans = 0
        for right in range(1, n):
            for left in range(0, right):
                diff = arr[right] - arr[left]
                dp[right][diff] = dp[left].get(diff, 1) + 1
                ans = max(ans, dp[right][diff])
        return ans        
