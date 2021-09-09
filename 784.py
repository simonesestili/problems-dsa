class Solution:
	def letterCasePermutation(self, s: str) -> List[str]:
		permutations = []
		self.permute(s, '', 0, permutations)
		return permutations
	
	def permute(self, s, curr, idx, perms):
		if len(curr) == len(s):
			perms.append(curr)
		else:
			if s[idx].isalpha():
				self.permute(s, curr + s[idx].swapcase(), idx + 1, perms)
			self.permute(s, curr + s[idx], idx + 1, perms)


