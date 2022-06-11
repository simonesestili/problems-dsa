class Solution:
    def matchReplacement(self, s, sub, mappings):
        m, n, mps = len(s), len(sub), defaultdict(set)
        for a, b in mappings: mps[a].add(b)
        
        for i in range(m - n + 1):
            valid = True
            for j in range(n):
                if s[i + j] != sub[j] and s[i + j] not in mps[sub[j]]:
                    valid = False
                    break
            if valid: return True
        return False
