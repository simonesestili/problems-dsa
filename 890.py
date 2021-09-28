class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        return [word for word in words if self.fix(word) == self.fix(pattern)]

    def fix(self, word):
        maps, word_num = {}, 0
        fixed = ''
        for c in word:
            if c not in maps:
                maps[c] = chr(ord('a') + word_num)
                word_num += 1
            fixed += maps[c]
        return fixed    
