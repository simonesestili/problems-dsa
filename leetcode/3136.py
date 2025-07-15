class Solution:
    def isValid(self, word):
        vowels = 'aeiou'
        return len(word) >= 3 and not any(c in word for c in '@#$') and any(c in vowels for c in word.lower()) and any(c.isalpha() and c not in vowels for c in word.lower())
