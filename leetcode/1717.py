class Solution:
    def maximumGain(self, s, x, y):
        s = list(s)
        a, b = 'ab', 'ba'

        def remove(s, t, p):
            ans, rem = 0, []
            for c in s:
                if c == t[1] and rem and rem[-1] == t[0]:
                    ans += p
                    rem.pop()
                    continue
                rem.append(c)
            return ans, rem

        if x < y:
            x, y = y, x
            a, b = b, a

        ans, s = remove(s, a, x)
        ans2, _ = remove(s, b, y)
        return ans + ans2

