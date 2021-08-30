class Solution:     
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		groups = {}
		for word in strs:
			counts = [0] * 26
			for letter in word:
				counts[ord(letter) - ord('a')] += 1
			counts = tuple(counts)
			groups[counts] = groups.get(counts, []) + [word]

		anagrams = []
		for key in groups:
			anagrams.append(groups[key])
		return anagrams 
