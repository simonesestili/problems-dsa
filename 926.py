class Solution:
    def minFlipsMonoIncr(self, s):
        n = flips = len(s)
        # Zeros to the right of i
        zeros = [0] * n
        count = 0
        for i in range(n - 1, -1, -1):
            zeros[i] = count
            count += s[i] == '0'
        # Ones to the left of and including 1
        ones = [0] * n
        count = 0
        for i in range(n):
            count += s[i] == '1'
            ones[i] = count
        for i in range(n):
            flips = min(flips, ones[i] + zeros[i])
        return min(flips, s.count('0'), s.count('1'))
