class Solution:
    def candy(self, ratings):
        n = len(ratings)
        r = sorted([(rating, i) for i, rating in enumerate(ratings)])
        candies, total = [0] * n, 0
        for rating, i in r:
            left = 0 if not i or rating == ratings[i - 1] else candies[i - 1]
            right = 0 if i == n - 1 or rating == ratings[i + 1] else candies[i + 1]
            candies[i] = max(left, right) + 1
            total += candies[i]
        return total
