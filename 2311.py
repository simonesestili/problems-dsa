class Solution:
    def longestSubsequence(self, s, k):
        n = len(s)
        size = curr = 0

        for i in range(n - 1, -1, -1):
            cand = curr | ((s[i] == '1') << n - 1 - i)
            if cand > k: continue
            curr = cand
            size += 1
        return size

