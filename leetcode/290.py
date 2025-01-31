class Solution:
    def wordPattern(self, pattern, s):
        if len(pattern) != s.count(' ') + 1:
            return False

        lets, words = {}, {}
        for let, word in zip(pattern, s.split(' ')):
            if word in words and words[word] != let:
                return False
            if let in lets and lets[let] != word:
                return False
            words[word] = let
            lets[let] = word

        return True
