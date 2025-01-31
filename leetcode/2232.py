class Solution:
    def minimizeResult(self, exp):
        num1, num2 = exp.split('+')
        m, n = len(num1), len(num2)

        ans, res = '', float('inf')
        for i in range(m):
            l = num1[:i] if i else ''
            lm = num1[i:]
            for j in range(n):
                rm = num2[:j+1]
                r = num2[j+1:] if j + 1 != n else ''
                val = int(l or '1') * (int(lm) + int(rm)) * int(r or '1')
                if val >= res: continue
                ans, res = f'{l}({lm}+{rm}){r}', val

        return ans
