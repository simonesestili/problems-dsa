class Solution:
    def minFlips(self, a, b, c):
        flips = 0
        for _ in range(32):
            k = (a & 1) + (b & 1)
            flips += not k if c & 1 else k
            a, b, c = a >> 1, b >> 1, c >> 1
        return flips
