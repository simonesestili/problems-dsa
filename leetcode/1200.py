class Solution:
    def minimumAbsDifference(self, arr):
        arr, best, ans = sorted(arr), float('inf'), []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < best:
                ans = [(arr[i - 1], arr[i])]
                best = diff
            elif diff == best:
                ans.append((arr[i - 1], arr[i]))
        return ans
