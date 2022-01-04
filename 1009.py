class Solution:
    def bitwiseComplement(self, n):
        return n ^ ((1 << len(bin(n)) - 2) - 1)
