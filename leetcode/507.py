class Solution:
    def checkPerfectNumber(self, num):
        total = int(num != 1)
        for i in range(2, int(sqrt(num)) + 1):
            if not num % i:
                total += i if i == num // i else i + num // i
        return total == num
