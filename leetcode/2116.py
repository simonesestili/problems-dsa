class Solution:
    def canBeValid(self, s, locked):
        if len(s) % 2: return False

        curr = 0
        for c, lock in zip(s, locked):
            curr += 1 if lock == '0' or c == '(' else -1
            if curr < 0: return False

        curr = 0
        for c, lock in zip(s[::-1], locked[::-1]):
            curr += 1 if lock == '0' or c == ')' else -1
            if curr < 0: return False

        return True
