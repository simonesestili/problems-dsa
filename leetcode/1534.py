class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        n, ans = len(arr), 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans += abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c
        return ans
