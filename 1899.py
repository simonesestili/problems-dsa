class Solution:
    def mergeTriplets(self, triplets, target):
        ca = cb = cc = 0
        x, y, z = target
        for a, b, c in triplets:
            if a > x or b > y or c > z: continue 
            ca, cb, cc = max(a, ca), max(b, cb), max(c, cc)
        return ca == x and cb == y and cc == z
