class Solution:
    def maxValue(self, n, x):

        def maximize(s):
            for i, c in enumerate(s):
                if x > int(c):
                    return s[:i] + str(x) + s[i:]
            return s + str(x)

        def minimize(s):
            for i, c in enumerate(s):
                if x < int(c):
                    return s[:i] + str(x) + s[i:]
            return s + str(x)

        return maximize(n) if n[0] != '-' else '-' + minimize(n[1:])
