class Solution:
    def canConvertString(self, s, t, k):
        if len(s) != len(t):
            return False
        moves = defaultdict(int)
        for i in range(len(s)):
            if s[i] != t[i]:
                moves[self.shift(s[i], t[i])] += 1
        for move in moves:
            if 26 * (moves[move] - 1) + move > k:
                return False
        return True

    def shift(self, a, b):
        diff = ord(b) - ord(a)
        return diff if diff > 0 else diff + 26
