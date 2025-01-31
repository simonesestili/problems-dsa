class Solution:
    def capitalizeTitle(self, s):
        return ' '.join(w.lower() if len(w) < 3 else w.title() for w in s.split())
