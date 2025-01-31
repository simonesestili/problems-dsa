class Solution:
    def totalFruit(self, fruits):
        best = right = unique = 0
        baskets = defaultdict(int)
        for left, fruit in enumerate(fruits):
            while right < len(fruits) and (unique < 2 or baskets[fruits[right]] > 0):
                unique += baskets[fruits[right]] == 0
                baskets[fruits[right]] += 1
                right += 1
            best = max(best, right - left)
            baskets[fruit] -= 1
            unique -= baskets[fruit] == 0
        return best
