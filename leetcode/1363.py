class Solution:
    def largestMultipleOfThree(self, digits):
        digits, total = sorted(digits, reverse=1), sum(digits)

        mod1 = nsmallest(2, [d for d in digits if d % 3 == 1])
        mod2 = nsmallest(2, [d for d in digits if d % 3 == 2])

        if total % 3 == 1:
            if mod1:
                digits.remove(mod1[0])
            else:
                digits.remove(mod2[0])
                digits.remove(mod2[1])
        elif total % 3 == 2:
            if mod2:
                digits.remove(mod2[0])
            else:
                digits.remove(mod1[0])
                digits.remove(mod1[1])

        i = 0
        while i < len(digits) and digits[i] == 0: i += 1
        if i and i == len(digits): return '0'
        return ''.join(map(str, digits[i:]))
