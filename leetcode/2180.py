class Solution:
    def countEven(self, num):
        ans = 0

        for i in range(2, num + 1):
            x = sum([int(d) for d in str(i)])
            print(i, x)
            if x % 2 == 0: ans += 1
        
        return ans
