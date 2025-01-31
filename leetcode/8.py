class Solution:
    def myAtoi(self, s):
        num, pos, s = 0, True, s.lstrip()
        if s and s[0] in '+-': s, pos = s[1:], s[0] == '+'

        for x in s:
            if not x.isdigit(): break
            num = num * 10 + int(x)

        return min((1 << 31) - 1, num) if pos else max(-(1 << 31), -num)
