class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewels = set(jewels)
        return sum(x in jewels for x in stones)
