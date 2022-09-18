class Solution:
    def countDaysTogether(self, aa, la, ab, lb):
        MON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def f(x):
            mm, dd = map(int, x.split('-'))
            return sum(MON[:mm-1]) + dd

        a = (f(aa), f(la))
        b = (f(ab), f(lb))

        return sum(a[0] <= i <= a[1] and b[0] <= i <= b[1] for i in range(1, 400))
