class Solution:
    def pathSum(self, root, target):
        memo = defaultdict(int)
        memo[0] = 1
        self.paths = 0

        def dfs(root, prevSum):
            if not root:
                return
            currSum = prevSum + root.val
            self.paths += memo[currSum - target]
            memo[currSum] += 1
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            memo[currSum] -= 1

        dfs(root, 0)

        return self.paths
