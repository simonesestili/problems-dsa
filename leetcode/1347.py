class Solution:
    def minSteps(self, s, t):
        n = len(s)
        delta, code = [0] * 26, lambda c: ord(c) - ord('a')
        for c in s: delta[code(c)] += 1

        steps = 0
        for c in t:
            delta[code(c)] -= 1
            if delta[code(c)] < 0:
                delta[code(c)] = 0
                steps += 1

        return steps

