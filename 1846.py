class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        n, curr = len(arr), 0
        count = [0] * (n + 1)
        for x in arr: count[min(x, n)] += 1

        most = 1
        for val in range(1, n + 1):
            most = min(val, most + count[val])

        return most
