class Solution:
    def sumOfThree(self, num):
        if num % 3: return []
        return [num // 3 - 1, num // 3, num // 3 + 1]
