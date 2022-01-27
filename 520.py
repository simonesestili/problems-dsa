class Solution:
    def detectCapitalUse(self, word):
        return word in [word.lower(), word.upper(), word.title()]
