class Solution:
    def minFlips(self, s):
        l, r = [0, 0], [0, 0]
        for i, x in enumerate(s):
            r[0] += i % 2 != int(x == '1')
            r[1] += i % 2 == int(x == '1')

        ans, n = min(r), len(s) % 2
        for i, x in enumerate(s):
            l[0] += i % 2 != int(x == '1')
            l[1] += i % 2 == int(x == '1')
            r[0] -= i % 2 != int(x == '1')
            r[1] -= i % 2 == int(x == '1')
            ans = min(ans, r[n^1] + l[1], r[n] + l[0])

        return ans
