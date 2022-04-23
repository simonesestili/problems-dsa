class Solution:
    def longestPalindrome(self, s):
        ans, count = 0, Counter(s)
        odd = False

        for c in count:
            ans += count[c] >> 1
            odd |= count[c] & 1

        return 2 * ans + odd
