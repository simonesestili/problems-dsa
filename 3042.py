class Solution:
    def countPrefixSuffixPairs(self, words):
        return sum(words[j].startswith(words[i]) and words[j].endswith(words[i]) for i in range(len(words)) for j in range(i + 1, len(words)))
