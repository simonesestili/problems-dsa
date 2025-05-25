class Solution:
    def findWordsContaining(self, words, x):
        return [i for i, word in enumerate(words) if x in word]
