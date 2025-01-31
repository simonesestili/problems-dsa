class Solution:
    def maxDistance(self, arrays):
        ans, mn, mx = 0, arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            ans = max(ans, arr[-1] - mn, mx - arr[0])
            mn, mx = min(mn, arr[0]), max(mx, arr[-1])
        return ans

