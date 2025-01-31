class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        count = rightmost = 0
        for i in range(n):
            rightmost = max(rightmost, light[i]) 
            if rightmost == i + 1:
                count += 1
        return count
