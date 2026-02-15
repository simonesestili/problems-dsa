class Solution:
    def addBinary(self, a, b):
        ans, rem = [], 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            rem += int(x == '1') + int(y == '1')
            ans.append(str(rem & 1))
            rem >>= 1
        if rem: ans.append('1')
        return ''.join(reversed(ans))
