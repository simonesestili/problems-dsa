class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        valid = lambda a, b: len(a) == len(b) and sum(c1 != c2 for c1, c2 in zip(a, b)) == 1

        @cache
        def dp(i):
            ans = [words[i]]
            for j in range(i):
                if groups[j] != groups[i] and valid(words[j], words[i]):
                    ansj = dp(j)
                    if len(ansj) + 1 > len(ans):
                        ans = ansj + [words[i]]
            return ans

        return max((dp(i) for i in range(len(words))), key=len)
