class Solution:
    def countOdds(self, low, high):
        return (high - low) // 2 + max(low % 2, high % 2)
