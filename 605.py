class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = planted = 0
        l = len(flowerbed)
        while i < l:
            if flowerbed[i]:
                i += 1
                continue
            left, right = i - 1, i + 1
            if (left < 0 or not flowerbed[left]) and (right >= l or not flowerbed[right]):
                planted += 1
                i += 1
            i += 1    
        return n <= planted
