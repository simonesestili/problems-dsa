class Solution:
    def wordPattern(self, pattern, s):
        pairs, s, pattern = {}, s.split(), list(pattern)
        if len(s) != len(pattern): return False
        used = set()
        for p, w in zip(pattern, s):
            if p not in pairs:
                if w in used: return False
                pairs[p] = w
            if pairs[p] != w: return False
            used.add(w)
        return True

