class Solution:
    def arrangeWords(self, text):
        words = [(word, i) for i, word in enumerate(text.lower().split())]
        words.sort(key=lambda w: (len(w[0]), w[1]))
        return ' '.join([w[0] for w in words]).capitalize()
