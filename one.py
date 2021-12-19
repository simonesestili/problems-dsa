class Solution:
    def firstPalindrome(self, words):
        for word in words:
            if self.isvalid(word):
                return word
        return ''

    def isvalid(self, word):
        return word == word[::-1]
