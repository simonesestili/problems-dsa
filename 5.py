class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return (l + 1, r - 1)

        best = (0, 0)
        for i in range(1, n):
            even, odd = expand(i - 1, i), expand(i, i)
            if even[1] - even[0] > best[1] - best[0]:
                best = even
            if odd[1] - odd[0] > best[1] - best[0]:
                best = odd

        return s[best[0]:best[1]+1]
