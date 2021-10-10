class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        order = sorted([i for i in range(n)], key=lambda i: -arr[i])
        dp = [-1] * n
        
        while order:
            idx = order.pop()
            dp[idx] = max(dp[idx], 1)
            left, currMax = idx - 1, arr[idx]
            while left >= 0 and idx - left <= d:
                if arr[left] > currMax:
                    currMax = arr[left]
                    dp[left] = max(dp[left], dp[idx] + 1)
                left -= 1    
            right, currMax = idx + 1, arr[idx] 
            while right < n and right - idx <= d:
                if arr[right] > currMax:
                    currMax = arr[right]
                    dp[right] = max(dp[right], dp[idx] + 1)
                right += 1
        return max(dp)                    
