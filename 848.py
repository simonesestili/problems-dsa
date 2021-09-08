class Solution:
	def shiftingLetters(self, s: str, shifts: List[int]) -> str:
		total = 0
		for i in range(len(s) - 1, -1, -1):
			total += shifts[i]
			shifts[i] = self.shift(s[i], total)
		return ''.join(shifts)
				

	def shift(self, letter, n):
		return chr((ord(letter) - ord('a') + n) % 26 + ord('a'))
