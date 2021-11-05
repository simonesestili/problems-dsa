class Solution:
    def simplifiedFractions(self, n):
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        ans = []
        for denom in range(2, n + 1):
            for num in range(1, denom):
                if gcd(num, denom) == 1:
                    ans.append(str(num) + '/' + str(denom))
        return ans
