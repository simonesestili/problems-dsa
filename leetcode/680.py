class Solution:
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1

        def valid_palin(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i, j = i + 1, j - 1
            return True

        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
                continue
            if valid_palin(left + 1, right) or valid_palin(left, right - 1):
                break
            return False

        return True
