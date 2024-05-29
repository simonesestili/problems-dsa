class Solution:
    def numberOfPairs(self, a, b, k):
        ans = 0
        for i in a:
            for j in b:
                ans += i % (j * k) == 0
        return ans

