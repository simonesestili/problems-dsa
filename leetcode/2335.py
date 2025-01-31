class Solution:
    def fillCups(self, amount):
        s, amount = 0, sorted(amount)
        while amount[-1]:
            amount[-1] -= 1
            amount[-2] -= amount[-2] != 0
            amount.sort()
            s += 1
        return s
