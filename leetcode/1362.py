class Solution:
    def closestDivisors(self, num):
        cand1 = self.closest(num + 1)
        cand2 = self.closest(num + 2)
        if abs(cand1[0] - cand1[1]) < abs(cand2[0] - cand2[1]):
            return cand1
        return cand2

    def closest(self, num):
        for i in range(floor(sqrt(num)), 1, -1):
            if not num % i:
                return [i, num // i]
        return [1, num]
