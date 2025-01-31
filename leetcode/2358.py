class Solution:
    def maximumGroups(self, grades):
        return int(math.sqrt(1 + 8 * len(grades)) - 1) // 2
