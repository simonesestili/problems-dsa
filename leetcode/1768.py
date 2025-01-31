class Solution:
    def mergeAlternately(self, word1, word2):
        ans = []
        for a, b in zip_longest(word1, word2, ''):
            ans.append(a)
            ans.append(b)
        return ''.join(ans)
