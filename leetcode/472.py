class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        ans, seen = [], set()

        def valid(word):
            dp = [True] + [False] * len(word)
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if not dp[j] or word[j:i] not in seen: continue
                    dp[i] = True
                    break
            return dp[-1]

        for word in sorted(words, key=len):
            if valid(word):
                ans.append(word)
            seen.add(word)
        return ans
