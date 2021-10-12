class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        pattern = []
        idx = n - 1
        while idx > 0:
            if p[idx] == '*':
                wild = (p[idx - 1], p[idx])
                if pattern[-1] != wild:
                    pattern.append(wild)
                idx -= 2
            else:
                pattern.append((p[idx], ''))
                idx -= 1
        pattern = pattern[::-1]
        print(pattern)
        
