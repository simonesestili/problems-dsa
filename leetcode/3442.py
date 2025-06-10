class Solution:
    def maxDifference(self, s):
        cnts = Counter(s).values()
        return max(cnt for cnt in cnts if cnt % 2) - min(cnt for cnt in cnts if not cnt % 2)
