class Solution:
    def breakPalindrome(self, palindrome):
        n, palindrome = len(palindrome), list(palindrome)
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[-1] = 'b'
        return '' if n == 1 else ''.join(palindrome)
