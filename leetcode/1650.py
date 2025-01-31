class Solution:
    def lowestCommonAncestor(self, p, q):
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        while q:
            if q in seen: return q
            q = q.parent
        return None
