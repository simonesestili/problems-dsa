class Solution:
    def maxProduct(self, words):
        best, n = 0, len(words)
        chars = [set(word) for word in words]
        for i in range(n):
            for j in range(i):
                if not chars[i] & chars[j]:
                    best = max(best, len(words[i]) * len(words[j]))
        return best
