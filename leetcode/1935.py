class Solution:
    def canBeTypedWords(self, text, broken):
        broken = set(broken)
        return sum(all(c not in broken for c in w) for w in text.split(' '))
