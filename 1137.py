class Solution:
    def tribonacci(self, n):
        trib = [0, 1, 1]
        if n < 3:
            return trib[n]
        while n > 2:
            trib = [trib[1], trib[2], sum(trib)]
            n -= 1
        return trib[-1]    
