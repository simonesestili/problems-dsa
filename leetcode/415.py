class Solution:
    def addStrings(self, num1, num2):
        ans, carry = [], 0
        for a, b in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            val = carry + int(a) + int(b)
            ans.append(str(val % 10))
            carry = val // 10
        if carry: ans.append(str(carry))
        return ''.join(ans[::-1])

