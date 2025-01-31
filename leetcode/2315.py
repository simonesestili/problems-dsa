class Solution:
    def countAsterisks(self, s):
        count, counting = 0, True
        for c in s:
            if c == '|': counting = not counting
            elif c == '*': count += counting
        return count
