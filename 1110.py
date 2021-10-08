# Faster than 99.74%
class Solution:
    def delNodes(self, root, toDelete):
        toDelete = set(toDelete)
        forest = []

        def getForest(root, isRoot):
            if not root:
                return root
            isInvalid = root.val in toDelete
            if isInvalid:
                getForest(root.left, isInvalid)
                getForest(root.right, isInvalid)
                return
            if isRoot:
                forest.append(root)
            root.left = getForest(root.left, isInvalid)
            root.right = getForest(root.right, isInvalid)
            return None if isInvalid else root
        
        getForest(root, True)
        return forest
