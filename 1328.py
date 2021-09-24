class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        broken = ''
        for i in range(n // 2):
            if palindrome[i] != 'a':
                broken += 'a'
                return broken + palindrome[i + 1:]
            broken += palindrome[i]
        return palindrome[:-1] + 'b'    
