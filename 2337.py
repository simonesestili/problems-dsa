class Solution:
    def canChange(self, start, target):
        extract = lambda arr: [(val, i) for i, val in enumerate(arr) if val != '_']
        start, target = extract(start), extract(target)
        if len(start) != len(target): return False
        if any(v1 != v2 for (v1, i), (v2, j) in zip(start, target)): return False

        for (v1, i), (v2, j) in zip(start, target):
            if v1 == 'R' and j < i: return False
            if v1 == 'L' and j > i: return False

        return True
