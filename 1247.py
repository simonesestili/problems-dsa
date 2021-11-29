class Solution:
    def minimumSwap(self, s1, s2):
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a != b:
                xy += a == 'x'
                yx += a == 'y'
        return -1 if (xy + yx) % 2 else (xy // 2) + (yx // 2) + 2 * (xy % 2)

##############################################################################

class Solution: # O(n^2) Time
    def minimumSwap(self, s1, s2):
        n = len(s1)
        x, y = s1.count('x') + s2.count('x'), s1.count('y') + s2.count('y')
        if x % 2 or y % 2:
            return -1
        swaps, s1, s2 = 0, list(s1), list(s2)
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            for j in range(i + 1, n):
                if s2[j] != s1[i] and s2[j] != s1[j]:
                    s1[i], s2[j] = s2[j], s1[i]
                    break
            swaps += 1
        return swaps
