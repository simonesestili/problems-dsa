class Solution:
    def longestPalindrome(self, words):
        ans, count = 0, Counter(words)
        mid = 0
        for word in count:
            if word[0] == word[1]:
                ans += count[word] - count[word] % 2
                mid += count[word] % 2
            else:
                ans += min(count[word], count[word[::-1]])
        return (ans + min(1, mid)) * 2
