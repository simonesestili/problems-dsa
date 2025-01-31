class Solution:
    def permute(self, nums):
        self.permutations = []

        def dfs(curr=[]):
            if len(curr) == len(nums):
                self.permutations.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(curr)
                    curr.pop()

        dfs()
        return self.permutations
