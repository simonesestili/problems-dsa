class Solution:
    def canBeEqual(self, a, b):
        return sorted([a[0], a[2]]) == sorted([b[0], b[2]]) and sorted([a[1], a[3]]) == sorted([b[1], b[3]])
