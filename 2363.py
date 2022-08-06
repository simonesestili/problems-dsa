class Solution:
    def mergeSimilarItems(self, a, b):
        weights = defaultdict(int)
        for v, w in a: weights[v] += w
        for v, w in b: weights[v] += w
        return [[key, weights[key]] for key in sorted(weights.keys())]
