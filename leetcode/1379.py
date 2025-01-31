class Solution:
    def getTargetCopy(self, orig, clone, t):
        if not orig: return None
        if orig is t: return clone
        return self.getTargetCopy(orig.left, clone.left, t) or self.getTargetCopy(orig.right, clone.right, t)
