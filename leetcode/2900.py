class Solution:
    def getLongestSubsequence(self, words, groups):
        ans, prev = [], -1
        for word, val in zip(words, groups):
            if val == prev: continue
            ans.append(word)
            prev = val
        return ans
