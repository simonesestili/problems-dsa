class Solution:
    def maximumProfit(self, prices, k):
        flat = [0] + [-inf] * k
        long = [-inf] * (k + 1)
        short = [-inf] * (k + 1)

        for p in prices:
            new_flat = flat[:]
            new_long = long[:]
            new_short = short[:]

            for t in range(k + 1):
                if long[t] != -inf:
                    new_flat[t] = max(new_flat[t], long[t] + p)
                if short[t] != -inf:
                    new_flat[t] = max(new_flat[t], short[t] - p)
                if t < k and flat[t] != -inf:
                    new_long[t + 1]  = max(new_long[t + 1],  flat[t] - p)
                    new_short[t + 1] = max(new_short[t + 1], flat[t] + p)

            flat, long, short = new_flat, new_long, new_short

        return max(flat)
