class Solution:
    def doesValidArrayExist(self, derived):
        return reduce(xor, derived) == 0
