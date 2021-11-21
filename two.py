class Solution:
    def wateringPlants(self, plants, cap):
        n = len(plants)
        steps, curr = 0, cap
        for i in range(n):
            curr -= plants[i]
            if i != n - 1 and curr < plants[i + 1]:
                steps += 2 * (i + 1)
                curr = cap
            steps += 1
        return steps
