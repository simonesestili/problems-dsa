class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0
        while n != 1:
            if n == 3:
                return operations + 2

            if n % 2 == 0:
                n /= 2
            elif self.twos(n - 1) >= self.twos(n + 1):
                n -= 1
            else:
                n += 1

            operations += 1
        return operations

    def twos(self, n):
        count = 0
        while n % 2 == 0:
            n /= 2
            count += 1
        return count
