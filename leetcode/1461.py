class Solution:
    def hasAllCodes(self, s, k):
        if len(s) < k: return False
        req, mask = 1 << k, (1 << k-1) - 1

        seen, curr = set(), 0
        for i, x in enumerate(s):
            curr = (curr << 1) + (x == '1')
            if i < k-1: continue
            req -= curr not in seen
            seen.add(curr)
            if not req: return True
            curr &= mask

        return False
