class Solution:
    def minMaxDifference(self, num):
        num = str(num)
        mx = num.replace(next(filter(lambda d: d != '9', num), '9'), '9')
        mn = num.replace(num[0], '0')
        return int(mx) - int(mn)
