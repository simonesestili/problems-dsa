class Solution:
    def maxConsecutive(self, bot, top, special):
        special = [bot - 1] + sorted(special) + [top + 1]
        return max(special[i] - special[i-1] - 1 for i in range(1, len(special)))
