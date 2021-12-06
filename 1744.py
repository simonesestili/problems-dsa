class Solution:
    def canEat(self, candies, queries):
        prefix = [0]
        for i in range(len(candies) - 1):
            prefix.append(prefix[-1] + candies[i])
        return [prefix[i] // cap <= day < prefix[i] + candies[i] for i, day, cap in queries]
