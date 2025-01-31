class Solution:
    def addBinary(self, b1, b2):
        ans, carry = [], 0
        for a, b in zip_longest(b1[::-1], b2[::-1], fillvalue='0'):
            carry += (a == '1') + (b == '1')
            ans.append(str(carry & 1))
            carry >>= 1
        if carry: ans.append(str(carry))
        return ''.join(ans[::-1])
