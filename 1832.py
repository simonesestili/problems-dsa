class Solution:     
	def checkIfPangram(self, sentence: str) -> bool: 
		letters = [False] * 26
		for letter in sentence:
			letters[ord(letter) - ord('a')] = True
		return all(letters)
