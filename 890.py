class Solution:
    def findAndReplacePattern(self, words, pattern):
        
        def fix(word):
            mp, fixed, offset = {}, [], 0
            for c in word:
                if c not in mp:
                    mp[c] = chr(ord('a') + offset)
                    offset += 1
                fixed.append(mp[c])
            return ''.join(fixed)

        pattern = fix(pattern)
        return [word for word in words if fix(word) == pattern]
