class Solution:
    def strongPasswordCheckerII(self, p):
        has_lower, has_upper = any(c.islower() for c in p), any(c.isupper() for c in p)
        has_dig, has_spe = any(c.isdigit() for c in p), any(not (c.isdigit() or c.isalpha()) for c in p)
        has_adj = any(p[i-1] == p[i] for i in range(1, len(p)))
        return len(p) >= 8 and has_lower and has_upper and has_dig and has_spe and not has_adj
