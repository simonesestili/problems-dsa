class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        letters = [0] * 26
        for word in words:
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
        for count in letters:
            if count % n != 0:
                return False
        return True