class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        smallest = ''
        while n > 0:
            for i in range(26):
                if k - i - 1 <= (n - 1) * 26:
                    smallest += chr(ord('a') + i)
                    k -= i + 1
                    n -= 1
                    break
        return smallest
