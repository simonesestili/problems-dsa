class Solution:
    def possibleStringCount(self, word):
        return 1 + sum(len(list(vals)) - 1 for _, vals in groupby(word))
