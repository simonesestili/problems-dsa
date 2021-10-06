class Solution:
    def beautySum(self, s: str) -> int:
        n, beauty = len(s), 0
        for i in range(n - 2):
            freqs = [0] * 26
            for j in range(i, n):
                freqs[ord(s[j]) - ord('a')] += 1
                beauty += max(freqs) - min(freq for freq in freqs if freqs)
        return beauty        
