class Solution(object):     
    def reverseOnlyLetters(self, s):
        reversed_letters = [letter for letter in s if letter.isalpha()]
        reversed_letters.reverse()
        result, idx = '', 0
        for letter in s:
            if letter.isalpha():
                result += reversed_letters[idx]
                idx += 1
            else:
                result += letter
        return result        
