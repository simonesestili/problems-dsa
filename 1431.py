class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [(candies[i] + extraCandies) >= greatest for i in range(len(candies))]