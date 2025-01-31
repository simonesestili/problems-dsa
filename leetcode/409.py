class Solution:
    def longestPalindrome(self, s):
        ans, odd, counts = 0, False, Counter(s)
        for count in counts.values():
            ans += count // 2
            odd |= count % 2
        return 2 * ans + odd

