class Solution:
    def countOfAtoms(self, formula):
        counts, stack, coef, mul, p, elem = defaultdict(int), [], 1, 1, 1, ''

        for c in reversed(formula):
            if c.isdigit():
                coef = int(c) if coef == p == 1 else int(c) * p + coef
                p *= 10
            elif c == ')':
                stack.append(coef)
                mul *= coef
                coef = p = 1
            elif c == '(':
                mul //= stack.pop()
            elif c.islower():
                elem += c
            elif c.isupper():
                elem += c
                counts[elem[::-1]] += coef * mul
                coef = p = 1
                elem = ''

        return ''.join((f'{elem}{counts[elem] if counts[elem] != 1 else ""}' for elem in sorted(counts.keys())))

