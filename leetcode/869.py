class Solution:
    def reorderedPowerOf2(self, n):
        target, curr = Counter(str(n)), 1
        for _ in range(32):
            if Counter(str(curr)) == target:
                return True
            curr <<= 1
        return False
