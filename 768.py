class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        mn, mx = arr[:], arr[:]
        for i in range(1, n): mx[i] = max(mx[i], mx[i-1])
        for i in range(n - 2, -1, -1): mn[i] = min(mn[i], mn[i+1])

        return 1 + sum(mx[i] <= mn[i+1] for i in range(n - 1))
