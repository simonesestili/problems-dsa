class Solution:
    def countNumbersWithUniqueDigits(self, n):
        ans, prod, curr = 1, 9, 9
        for i in range(n):
            ans += prod
            prod *= curr
            curr -= 1
        return ans
