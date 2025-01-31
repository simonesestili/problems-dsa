class Solution:
    def smallestNumber(self, n):
        if n == 0: return 0
        s = str(n)

        if n < 0:
            return -int(''.join(sorted(s[1:], reverse=True)))

        s = sorted(s)
        y = -1
        for i, x in enumerate(s):
            if x != '0':
                y = i
                break

        return int(''.join([s[y]] + s[:y] + s[y + 1:]))

