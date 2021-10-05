class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        isPalin = [[False for x in range(n)] for y in range(n)]
        # Cache all subarrays
        for i in range(n):
            isPalin[i][i] = True
            diff = 1
            while i - diff >= 0 and i + diff < n:
                if s[i - diff] != s[i + diff]:
                    break
                isPalin[i - diff][i + diff] = True
                diff += 1
            if i == n - 1:
                break
            if s[i] == s[i + 1]:
                isPalin[i][i + 1] = True
                diff = 1
                while i - diff >= 0 and i + 1 + diff < n:
                    if s[i - diff] != s[i + 1 + diff]:    
                        break
                    isPalin[i - diff][i + 1 + diff] = True
                    diff += 1

        # Check for valid partitions
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if isPalin[0][i] and isPalin[i + 1][j] and isPalin[j + 1][-1]:
                    return True

        return False
