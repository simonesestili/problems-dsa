class Solution:
    def findLongestWord(self, s, words):
        
        def valid(word):
            i = 0
            for c in word:
                while i < len(s) and s[i] != c: i += 1
                if i == len(s): return False
                i += 1
            return True

        for w in sorted(words, key=lambda w: (-len(w), w)):
            if valid(w): return w

        return ''
