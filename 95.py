class Solution:
    def generateTrees(self, n):

        @cache
        def generate(l, r):
            trees = []
            for i in range(l, r + 1):
                for left in generate(l, i - 1):
                    for right in generate(i + 1, r):
                        trees.append(TreeNode(i, left, right))
            return trees if trees else [None]

        return generate(1, n)
