class Solution:
    def minimumAbsDifference(self, arr):
        ans, arr = [], sorted(arr)
        for i in range(1, len(arr)):
            if not ans or arr[i] - arr[i-1] == ans[-1][1] - ans[-1][0]:
                ans.append([arr[i-1], arr[i]])
            elif ans and arr[i] - arr[i-1] < ans[-1][1] - ans[-1][0]:
                ans = [[arr[i-1], arr[i]]]
        return ans
