class Solution:
    def frequencySort(self, s):
        freqs = defaultdict(int)
        for c in s:
            freqs[c] -= 1
        order = []
        for c in freqs:
            order.append((freqs[c], c))
        order.sort()
        return ''.join([char * -count for count, char in order])