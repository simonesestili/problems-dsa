class Solution:
	def letterCasePermutation(self, s: str) -> List[str]:
        perms = []

        def build(i=0, curr=''):
            if i == len(s):
                perms.append(curr)
            elif s[i].isalpha():
                build(i + 1, curr + s[i].lower())
                build(i + 1, curr + s[i].upper())
            else:
                build(i + 1, curr + s[i])

        build()
        return perms
