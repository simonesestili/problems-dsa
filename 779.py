class Solution:     
    def kthGrammar(self, n: int, k: int) -> int:
        pos = k / (2 ** (n - 1))
        curr, interval = 0, [0, 1]
        while n > 1:
            mid = sum(interval) / 2
            if pos > mid:
                curr = 0 if curr else 1    
                interval[0] = mid
            else:
                interval[1] = mid
            n -= 1

        return curr
