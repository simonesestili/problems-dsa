class Solution:
    def longestPalindrome(self, words):
        ans = mid = 0
        seen = defaultdict(int)
        for word in words:
            if seen[word[::-1]]:
                seen[word[::-1]] -= 1
                mid -= word[0] == word[1]
                ans += 4
            else:
                seen[word] += 1
                mid += word[0] == word[1]
        return ans + (2 if mid else 0)
