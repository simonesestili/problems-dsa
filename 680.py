class Solution(object):     
    def validPalindrome(self, s): 
        left, right = 0, len(s) - 1
        removed = False
        for i in range(len(s) // 2):
            if s[left] != s[right]:
                if removed:
                    return False

                if s[left + 1] == s[right]:
                    left += 1
                elif s[left] == s[right - 1]:
                    right -= 1
                else:
                    return False

                removed = True
            left += 1
            right -= 1

        return True
