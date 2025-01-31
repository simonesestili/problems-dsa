class Solution:
    def convertTime(self, curr, corr):
        ans = 0

        def f(x):
            hh, mm = map(int, x.split(':'))
            return hh * 60 + mm

        diff = f(corr) - f(curr)
        for t in [60, 15, 5, 1]:
            ans += diff // t
            diff %= t

        return ans
