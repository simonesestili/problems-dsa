class Solution:
    def countPoints(self, rings):
        poles = [set() for _ in range(10)]
        for i in range(len(rings) // 2):
            poles[ord(rings[i * 2 + 1]) - ord('0')].add(rings[i * 2])
        return len([0 for i in range(10) if len(poles[i]) == 3])
