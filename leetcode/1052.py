class Solution:
    def maxSatisfied(self, customers, grumpy, m):
        base = sum(c for c, g in zip(customers, grumpy) if not g)
        best = curr = l = 0

        for r in range(len(customers)):
            if grumpy[r]: curr += customers[r]
            if r - l + 1 > m:
                if grumpy[l]: curr -= customers[l]
                l += 1
            best = max(best, curr)

        return base + best

