class Solution:
    def reorderedPowerOf2(self, n):
        digs, curr = Counter(str(n)), 1
        for _ in range(31):
            if Counter(str(curr)) == digs:
                return True
            curr <<= 1
        return False
