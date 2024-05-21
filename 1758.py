class Solution:
    def minOperations(self, s):
        a = b = 0
        for i, c in enumerate(s):
            a += c == '1' if i % 2 else c != '1'
            b += c == '0' if i % 2 else c != '0'
        return min(a, b)
