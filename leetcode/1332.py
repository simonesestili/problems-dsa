class Solution:
    def removePalindromeSub(self, s):
        return 1 + any(s[i] != s[-1-i] for i in range(len(s) // 2))
