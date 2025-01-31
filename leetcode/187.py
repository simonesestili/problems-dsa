import collections
class Solution:
	def findRepeatedDnaSequences(self, s: str) -> List[str]:
		sequence_count = collections.defaultdict(int)
		
		for start in range(len(s) - 9):
			sequence_count[s[start:start+10]] += 1
		
		return [seq for seq in sequence_count if sequence_count[seq] > 1]
