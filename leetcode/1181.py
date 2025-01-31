class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        n = len(phrases)
        ans, phrases = set(), [sentence.split() for sentence in phrases]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if phrases[i][-1] == phrases[j][0]:
                    ans.add(' '.join(phrases[i] + phrases[j][1:]))
        return sorted(ans)

