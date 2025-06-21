class Solution:
    def minimumDeletions(self, word, k):
        ans, cnts = inf, Counter(word)
        for mn in range(0, len(word) + 1):
            cand = 0
            for c in cnts:
                if cnts[c] < mn: cand += cnts[c]
                elif cnts[c] > mn + k: cand += cnts[c] - mn - k
            ans = min(ans, cand)
        return ans
