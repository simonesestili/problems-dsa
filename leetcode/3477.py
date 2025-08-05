class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        ans = n = len(fruits)
        for f in fruits:
            for i in range(n):
                if baskets[i] >= f:
                    ans -= 1
                    baskets[i] = 0
                    break
        return ans
