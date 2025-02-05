class Solution:
    def areAlmostEqual(self, s1, s2):
        idxs = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        return len(idxs) == 0 if len(idxs) != 2 else s1[idxs[0]] == s2[idxs[1]] and s1[idxs[1]] == s2[idxs[0]]
