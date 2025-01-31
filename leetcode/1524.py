class Solution:
    def numOfSubarrays(self, arr):
        n = len(arr)
        evens, odds = [0] * n, [0] * n
        evens[0] += not arr[0] % 2
        odds[0] += arr[0] % 2
        for i in range(1, n):
            evens[i] = odds[i - 1] if arr[i] % 2 else 1 + evens[i - 1]
            odds[i] = 1 + evens[i - 1] if arr[i] % 2 else odds[i - 1]
        return sum(odds) % (10**9 + 7)
