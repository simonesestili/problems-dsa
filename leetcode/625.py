class Solution:
    def smallestFactorization(self, num):
        if num == 1: return 1
        self.digits, self.num = [], num

        def extract(i):
            while not self.num % i:
                self.digits.append(i)
                self.num //= i

        for i in range(9, 1, -1): extract(i)
        if self.num != 1: return 0
        ans = int(''.join(map(str, sorted(self.digits))))
        return 0 if ans > 1 << 31 else ans

