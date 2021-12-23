class Solution:
    def concatenatedBinary(self, n):
        M, curr = pow(10, 9) + 7, 1
        for i in range(2, n + 1):
            curr = ((curr << (int(log2(i)) + 1)) % M + i) % M
        return curr
