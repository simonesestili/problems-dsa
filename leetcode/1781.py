class Solution:
    def beautySum(self, s):
        n, ans = len(s), 0
        for i in range(n - 2):
            freqs = [0] * 26
            for j in range(i, n):
                freqs[ord(s[j]) - ord('a')] += 1
                ans += max(freqs) - min([x for x in freqs if x])
        return ans
