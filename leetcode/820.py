class Solution:
    def minimumLengthEncoding(self, words):
        uniques = set(words)

        for word in words:
            for sub in range(1, len(word)):
                uniques.discard(word[-sub:])

        return sum(map(lambda w: len(w) + 1, uniques))
