class Solution:
    def categorizeBox(self, l, w, h, m):
        bulky = max(l, w, h) >= 10 ** 4 or l * w * h >= 10 ** 9
        heavy = m >= 100
        if bulky and heavy: return 'Both'
        if bulky: return 'Bulky'
        if heavy: return 'Heavy'
        return 'Neither'
