class Solution:
    def countSymmetricIntegers(self, low, high):
        def valid(x):
            n = len(x)
            return n % 2 == 0 and sum(map(int, x[:n//2])) == sum(map(int, x[n//2:]))
        return sum(valid(str(i)) for i in range(low, high + 1))
