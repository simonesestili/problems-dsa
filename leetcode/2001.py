class Solution:
    def interchangeableRectangles(self, rects):
        count, ratios = 0, defaultdict(int)
        for w, h in rects:
            common = gcd(w, h)
            ratio = (w // common, h // common)
            count += ratios[ratio]
            ratios[ratio] += 1
        return count
