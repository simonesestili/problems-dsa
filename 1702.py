class Solution:
    def maximumBinaryString(self, s):
        n, zero = len(s), s.count('0')
        if zero < 2: return s

        ones, first = n - zero, s.index('0')
        return '1' * (first + zero - 1) + '0' + '1' * (ones - first)
