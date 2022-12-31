class Solution:
    def similarPairs(self, words):
        ans = 0
        for i in range(len(words)):
            for j in range(i):
                if set(words[i]) == set(words[j]):
                    ans += 1
        return ans
