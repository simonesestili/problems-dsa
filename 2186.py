class Solution:
    def minSteps(self, s, t):
        code = lambda c: ord(c) - ord('a')
        counts = [0] * 26
        for c in s: counts[code(c)] += 1
        for c in t: counts[code(c)] -= 1
        return sum(map(abs, counts))
