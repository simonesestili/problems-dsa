class Solution:
    def calculateTax(self, brackets, income):
        tax = prev = 0
        for upper, percent in brackets:
            tax += max((min(income, upper) - prev) * percent / 100, 0)
            prev = upper
        return tax
