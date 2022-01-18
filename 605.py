class Solution:
    def canPlaceFlowers(self, flowerbed, k):
        n, i, flowers = len(flowerbed), 0, 0
        while i < n:
            if (not i or not flowerbed[i - 1]) and (i + 1 == n or not flowerbed[i + 1]) and (not flowerbed[i]):
                flowers += 1
                i += 1
            i += 1
        return flowers >= k
