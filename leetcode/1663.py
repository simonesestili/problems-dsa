class Solution:
    def getSmallestString(self, n, k):
        ans = []
        for i in range(n):
            c = max(k - (n - i - 1) * 26, 1)
            ans.append(chr(c + ord('a') - 1))
            k -= c
        return ''.join(ans)

