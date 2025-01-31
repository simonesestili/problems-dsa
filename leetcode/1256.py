class Solution:
    def encode(self, num):
        return bin(num + 1)[3:]
