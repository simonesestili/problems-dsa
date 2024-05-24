class Solution:
    def maxScoreWords(self, words, letters, score):
        curr = Counter(letters)
        words = [Counter(w) for w in words]
        scores = [sum(score[ord(ch)-ord('a')] * cn for ch, cn in w.items()) for w in words]

        def dfs(i, curr):
            ans = 0
            if i == len(words): return ans

            if all(curr[ch] >= cn for ch, cn in words[i].items()):
                curr -= words[i]
                ans = scores[i] + dfs(i+1, curr)
                curr += words[i]

            return max(ans, dfs(i+1, curr))
        
        return dfs(0, curr)

