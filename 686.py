class Solution:
    def repeatedStringMatch(self, a, b):
        repeated = ''
        while len(repeated) < len(b):
            repeated += a
        if b in repeated:
            return len(repeated) // len(a)
        repeated += a
        if b in repeated:
            return len(repeated) // len(a)
        return -1
