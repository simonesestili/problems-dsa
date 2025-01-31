class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for rating, i in sorted((ratings[i], i) for i in range(n)):
            if i and ratings[i-1] < rating:
                candies[i] = max(candies[i], candies[i-1] + 1)
            if i != n - 1 and ratings[i+1] < rating:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)
