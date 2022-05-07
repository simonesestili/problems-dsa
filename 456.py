class Solution:
    def find132pattern(self, nums):
        mono, mn = [], float('inf')

        for num in nums:
            mn = min(mn, num)
            while mono and mono[-1][0] <= num:
                mono.pop()
            if mono and mono[-1][1] < num:
                return True
            mono.append((num, mn))

        return False
            
