class Solution:
    def isNStraightHand(self, hand, size):
        n, count = len(hand), Counter(hand)
        if n % size: return False

        for val in sorted(count.keys()):
            if count[val-1] > 0 or count[val] == 0: continue
            c = count[val]
            for x in range(val, val + size):
                if c > count[x]: return False
                count[x] -= c

        return not any(count.values())
