class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [char for char in s.lower() if char.isalnum()]
        for i in range(len(chars) // 2):
            if chars[i] != chars[len(chars) - 1 - i]:
                return False
        return True
