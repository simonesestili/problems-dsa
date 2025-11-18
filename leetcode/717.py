class Solution:
    def isOneBitCharacter(self, bits):
        n, i = len(bits), 0
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1
