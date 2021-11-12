class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda p : (p[0], -p[1]))
        best_defense = -1
        weak = 0
        for i in range(len(properties) - 1, -1, -1):
            weak += properties[i][1] < best_defense
            best_defense = max(best_defense, properties[i][1])
        return weak
