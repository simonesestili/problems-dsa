class Solution:
    def maxNumberOfBalloons(self, text):
        text_letters = [0] * 26
        for letter in text:
            text_letters[ord(letter) - ord('a')] += 1
        balloon_letters = [0] * 26
        for letter in 'balloon':
            balloon_letters[ord(letter) - ord('a')] += 1
        minimum_letter = float('inf')
        for letter in 'balloon':
            val = ord(letter) - ord('a')
            minimum_letter = min(minimum_letter, text_letters[val] // balloon_letters[val])
        return minimum_letter    
