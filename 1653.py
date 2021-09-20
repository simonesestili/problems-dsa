class Solution:     
    def minimumDeletions(self, s: str) -> int: 
        n = len(s)
        aDeletions, aCount = [0] * n, 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                aCount += 1
            aDeletions[i] = aCount    
        least = aDeletions[0]
        bCount = 0
        for i in range(n):
            least = min(least, bCount + aDeletions[i])
            if s[i] == 'b':
                bCount += 1
        return min(least, bCount) 
