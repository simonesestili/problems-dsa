class Solution:
    def closestTarget(self, words, target, start):
        n = len(words)
        for d in range(n // 2 + 1):
            if target in (words[(start+d)%n], words[(start-d)%n]):
                return d
        return -1
