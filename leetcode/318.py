class Solution:
    def maxProduct(self, words):
        code = lambda c: ord(c) - ord('a')

        def get_mask(word):
            mask = 0
            for c in word:
                mask |= 1 << code(c)
            return mask

        best = 0
        words = [(get_mask(word), len(word)) for word in words]
        for i in range(len(words)):
            for j in range(i):
                if words[i][0] & words[j][0]: continue
                best = max(best, words[i][1] * words[j][1])

        return best
