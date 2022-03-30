class Solution:
    def countConsistentStrings(self, allowed, words):
        code = lambda c: ord(c) - ord('a')

        def extract(word, mask=0):
            for c in word: mask |= 1 << code(c)
            return mask

        ans = 0
        allowed = extract(allowed)
        for word in words:
            mask = extract(word)
            ans += mask & allowed == mask

        return ans
