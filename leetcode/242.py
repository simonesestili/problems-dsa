class Solution:
    def isAnagram(self, s, t):
        delta, code = [0] * 26, lambda c: ord(c) - ord('a')

        for c in s: delta[code(c)] += 1
        for c in t: delta[code(c)] -= 1

        return not any(delta)
