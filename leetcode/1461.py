class Solution:
    def hasAllCodes(self, s, k):
        return len({s[i:i+k] for i in range(len(s) - k + 1)}) == 1 << k
