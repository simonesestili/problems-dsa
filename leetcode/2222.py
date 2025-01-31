class Solution:
    def numberOfWays(self, s):
        rone, rzero = s.count('1'), s.count('0')
        one, zero = 0, 0
        ans = 0

        for i in range(len(s)):
            rone -= s[i] == '1'
            rzero -= s[i] == '0'
            if s[i] == '1':
                ans += rzero * zero
            else:
                ans += rone * one
            one += s[i] == '1'
            zero += s[i] == '0'

        return ans
