class Solution:
    def maximumBeauty(self, items, queries):
        ans, items = [], sorted(items)
        prices, values = [x[0] for x in items], [x[1] for x in items]
        for i in range(1, len(values)): values[i] = max(values[i], values[i - 1])

        for price in queries:
            idx = bisect_right(prices, price) - 1
            ans.append(0 if idx == -1 else values[idx])

        return ans
