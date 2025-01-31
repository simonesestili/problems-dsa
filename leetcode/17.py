class Solution:
    def letterCombinations(self, digits):
        self.mapping = {'2':'abc', '3':'def', '4':'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.combs = []
        
        def dfs(curr, i):
            if i == len(digits):
                self.combs.append(''.join(curr))
                return
            for letter in self.mapping[digits[i]]:
                dfs(curr + [letter], i + 1)

        dfs([], 0)
        return self.combs if self.combs[0] else []
