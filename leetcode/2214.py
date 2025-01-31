class Solution:
    def minimumHealth(self, damage, armor):
        best, prefix, suffix = float('inf'), 0, sum(damage)
        for x in damage:
            suffix -= x
            best = min(best, prefix + max(x - armor, 0) + suffix + 1)
            prefix += x
        return best
