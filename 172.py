class Solution:
    def trailingZeroes(self, n):
        count, i = 0, 1
        while 5 ** i <= n:
            count += n // 5 ** i
            i += 1
        return count
