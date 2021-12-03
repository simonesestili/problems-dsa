class Solution:
    def canConstruct(self, s, k):
        n = len(s)
        if k > n: 
            return False
        counts = Counter(s)
        odds = len([c for c in counts if counts[c] % 2])
        return odds <= k
