@cache
def check(rem, s):
    return any(check(rem - int(s[:i+1]), s[i+1:]) for i in range(len(s))) if s else rem == 0

class Solution:
    def punishmentNumber(self, n):
        return sum(i*i for i in range(1, n + 1) if check(i, str(i*i)))
