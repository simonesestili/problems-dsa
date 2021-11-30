class Solution:
    def countNumbersWithUniqueDigits(self, n):
        counts = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans = prod = 1
        for i in range(1, n + 1):
            prod *= counts[i - 1]
            ans += prod
        return ans
