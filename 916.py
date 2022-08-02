class Solution:
    def wordSubsets(self, words1, words2):
        max_counts = defaultdict(int)
        for word in words2:
            for c, count in Counter(word).items():
                max_counts[c] = max(max_counts[c], count)

        universals = []
        for word in words1:
            counts = Counter(word)
            for c, count in max_counts.items():
                if count > counts[c]: break
            else:
                universals.append(word)
        return universals

