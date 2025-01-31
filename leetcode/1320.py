class Solution:
    def minimumDistance(self, word):
        n, word = len(word), [ord(c) - ord('A') for c in word]

        @cache
        def dp(i, a, b):
            if i == n: return 0
            a_dist, b_dist = self.dist(word[i], a), self.dist(word[i], b)
            return min(a_dist + dp(i + 1, word[i], b), b_dist + dp(i + 1, a, word[i]))
            
        return min(dp(0, i, j) for i in range(26) for j in range(i))

    def dist(self, a, b):
        return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
