class Solution:
    def countVowels(self, word):
        n = len(word)
        VOWELS = set([c for c in 'aeiou'])
        return sum(0 if l not in VOWELS else (i + 1) * (n - i) for i, l in enumerate(word))
