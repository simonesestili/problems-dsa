class Solution:
    def uncommonFromSentences(self, s1, s2):
        counts = Counter(s1.split() + s2.split())
        return [word for word in counts if counts[word] == 1]
