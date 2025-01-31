class Solution:
    def countPairs(self, vals):
        n = len(vals)
        foods = collections.Counter(vals)
        count, maximum = 0, ceil(log2(max(vals))) + 1
        for i, val in enumerate(vals):
            foods[val] -= 1
            for i in range(maximum + 1):
                target = 2 ** i - val
                count += foods[target]
        return count % (10 ** 9 + 7)
