class Solution:
    def findKthBit(self, n, k):
        if n == 1: return '0'
        m = 1 << (n - 1)
        if k == m: return '1'
        if k < m: return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, 2 * m - k) == '0' else '0'
