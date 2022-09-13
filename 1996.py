class Solution:
    def numberOfWeakCharacters(self, properties):
        weak = best_defense = 0
        for attack, defense in sorted(properties, key=lambda x: (-x[0], x[1])):
            weak += defense < best_defense
            best_defense = max(best_defense, defense)
        return weak
