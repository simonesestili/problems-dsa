class Solution:
    def minOperations(self, n: int) -> int:
        return sum(range(n - 1, 0, -2))    
