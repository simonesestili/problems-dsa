class Solution:
    def isNStraightHand(self, hand, size):
        if len(hand) % size: return False

        counts = Counter(hand)
        for val in sorted(counts.keys()):
            if not counts[val]: continue
            c = counts[val]
            for i in range(size):
                if c > counts[val+i]: return False
                counts[val+i] -= c

        return True

