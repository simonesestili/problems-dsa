class Solution:
    def longestSubsequence(self, arr, diff):
        n, seen, ans = len(arr), defaultdict(int), 1
        for i in range(n - 1, -1, -1):
            curr = 1
            curr += seen[arr[i] + diff]
            seen[arr[i]] = curr
            ans = max(ans, curr)
        return ans
