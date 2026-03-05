class Solution:
    def minOperations(self, s):
        return min(cnt := sum(int(s[i]) == i & 1 for i in range(len(s))), len(s) - cnt)
