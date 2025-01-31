class Solution:
    def hasGroupsSizeX(self, deck):
        count = list(Counter(deck).values())
        x = count[0]
        for i in range(1, len(count)): x = gcd(x, count[i])
        return x > 1
