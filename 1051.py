class Solution:
    def heightChecker(self, heights):
        return sum(h != e for h, e in zip(heights, sorted(heights)))

