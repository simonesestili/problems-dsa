class Solution:
    def numberOfWays(self, corridor):
        ans, n, count = 1, len(corridor), corridor.count('S')
        if not count or count & 1: return 0
        M = pow(10, 9) + 7

        s = p = 0

        for c in corridor:
            s += c == 'S'
            p += s == 2 and c == 'P'
            if s > 2:
                ans = ans * (p + 1) % M
                p, s = 0, 1

        return ans
