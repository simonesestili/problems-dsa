class Solution:
    def checkIfCanBreak(self, s1, s2):
        x, y, n = sorted(s1), sorted(s2), len(s1)
        flag = 0 # note: 0 -> x == y  |  1 -> x > y  |  -1 -> y > x
        for i in range(n):
            comp = 0 if x[i] == y[i] else 1 if x[i] > y[i] else -1
            if not flag:
                flag = comp
            if comp and comp != flag:
                return False
        return True

