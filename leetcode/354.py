class Solution:
    def maxEnvelopes(self, envelopes):
        heights = [h for w, h in sorted(envelopes, key=lambda x: (x[0], -x[1]))]

        piles = []
        for h in heights:
            idx = bisect_left(piles, h)
            if idx == len(piles):
                piles.append(h)
            else:
                piles[idx] = h

        return len(piles)
