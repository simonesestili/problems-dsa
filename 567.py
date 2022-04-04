class Solution:
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        if m > n: return False
        delta, code = [0] * 26, lambda c: ord(c) - ord('a')

        for c in s1: delta[code(c)] += 1
        for i in range(m - 1): delta[code(s2[i])] -= 1

        for right in range(m - 1, n):
            delta[code(s2[right])] -= 1
            if not any(delta): return True
            delta[code(s2[right - m + 1])] += 1

        return False
