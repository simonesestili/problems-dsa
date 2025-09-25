class Solution:
    def fractionToDecimal(self, num, den):
        if not num:
            return '0'

        ans, num, den = ['-'] if num * den < 0 else [], abs(num), abs(den)
        ans.append(str(num // den))

        num %= den
        if not num:
            return ''.join(ans)

        idx = {}
        ans.append('.')
        while num:
            if num in idx:
                ans.insert(idx[num], '(')
                ans.append(')')
                break
            idx[num] = len(ans)
            num *= 10
            ans.append(str(num // den))
            num %= den

        return ''.join(ans)
