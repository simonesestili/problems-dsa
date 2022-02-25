class Solution:
    def compareVersion(self, v1, v2):
        v1 = list(map(int, v1.split('.')))
        v2 = list(map(int, v2.split('.')))

        for one, two in zip_longest(v1, v2, fillvalue=0):
            if one > two: return 1
            elif two > one: return -1
        return 0
