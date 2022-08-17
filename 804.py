MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
class Solution:
    def uniqueMorseRepresentations(self, words):
        return len({''.join(MORSE[ord(c)-ord('a')] for c in w) for w in words})
