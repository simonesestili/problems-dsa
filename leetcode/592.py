class Solution:
    def fractionAddition(self, exp):
        if exp[0] != '-': exp = '+' + exp

        n, d = 0, 1
        for frac in re.findall(r'[+-]\d+/\d+', exp):
            a, b = map(int, frac[1:].split('/'))
            if frac[0] == '-': a *= -1

            n = n * b + a * d
            d *= b

            gcd = math.gcd(n, d)
            n //= gcd
            d //= gcd

        return f'{n}/{d}'

