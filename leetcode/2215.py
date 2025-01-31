class Solution:
    def findDifference(self, a, b):
        return [set(a) - set(b), set(b) - set(a)]
