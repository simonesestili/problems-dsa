class Solution:
    def orderlyQueue(self, s, k):
        if k > 1: return ''.join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))
