class Solution:
	def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
		exact, caps, vowels = defaultdict(str), defaultdict(str), defaultdict(str)

		for word in wordlist[::-1]:
			exact[word] = word
			caps[word.lower()] = word
			vowels[self.unvowel(word)] = word
		return [exact[query] or caps[query.lower()] or vowels[self.unvowel(query)] or '' for query in queries] 

	
	def unvowel(self, s):
		return ''.join([letter if letter not in 'aeiou' else '#' for letter in s.lower()])
