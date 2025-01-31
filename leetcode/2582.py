class Solution:
    def passThePillow(self, n, time):
        d, m = divmod(time, n - 1)
        return n - m if d % 2 else m + 1

