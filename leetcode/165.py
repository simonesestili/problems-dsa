class Solution:
    def compareVersion(self, v1, v2):
        for a, b in zip_longest(map(int, v1.split('.')), map(int, v2.split('.')), fillvalue=0):
            if a > b: return 1
            elif a < b: return -1
        return 0
