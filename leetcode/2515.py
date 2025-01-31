class Solution:
    def closetTarget(self, word, target, start):
        if target not in word: return -1
        n = len(word)
        l = r = start
        for step in range(n):
            if target in (word[l], word[r]): return step
            l = (l - 1 + n) % n
            r = (r + 1 + n) % n
