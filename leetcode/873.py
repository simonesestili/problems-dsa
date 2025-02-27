class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)

        dp, vals = defaultdict(int), set(arr)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if arr[i] + arr[j] in vals:
                    dp[(arr[i], arr[j])] = 1 + dp.get((arr[j], arr[i] + arr[j]), 2)

        return max(dp.values(), default=0)
