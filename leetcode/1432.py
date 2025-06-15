class Solution:
    def maxDiff(self, num):
        num = str(num)

        x = next(filter(lambda d: d != '9', num), 'x')
        mx = num.replace(x, '9')

        x = next(filter(lambda d: d != '0' and (d != '1' or num[0] != '1'), num), 'x')
        mn = num.replace(x, '1' if x == num[0] else '0')

        return int(mx) - int(mn)
