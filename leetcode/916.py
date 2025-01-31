class Solution:
    def wordSubsets(self, words1, words2):
        counts = defaultdict(int)
        for w in words2:
            for c, cnt in Counter(w).items():
                counts[c] = max(counts[c], cnt)
        ans = []
        for w in words1:
            count = Counter(w)
            for c in counts:
                if counts[c] > count[c]: break
            else:
                ans.append(w)
        return ans
