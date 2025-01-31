class Solution:
    def newInteger(self, n):
        digits = []
        while n:
            digits.append(n % 9)
            n //= 9
        ans = 0
        while digits: ans = ans * 10 + digits.pop()
        return ans
