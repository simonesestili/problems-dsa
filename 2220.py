class Solution:
    def minBitFlips(self, start, goal):
        count = 0
        while start or goal:
            count += start & 1 != goal & 1
            start >>= 1
            goal >>= 1
        return count
