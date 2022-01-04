class Solution:
    def consecutiveNumbersSum(self, n):
        count, i = 0, 1
        while i * (i + 1) // 2 <= n:
            x = n / i - (i + 1) / 2
            count += int(x) == x
            i += 1
        return count
