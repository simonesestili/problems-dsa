class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        base, n = 0, len(customers)
        for i in range(n): base += 0 if grumpy[i] else customers[i]

        extra = 0
        for i in range(minutes): extra += customers[i] if grumpy[i] else 0
        ans = base + extra

        for i in range(minutes, n):
            if grumpy[i]: extra += customers[i]
            if grumpy[i - minutes]: extra -= customers[i - minutes]
            ans = max(ans, base + extra)

        return ans
