class Solution:     
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        idx = 0
        for c in t:
            if s[idx] == c:
                idx += 1
                if idx == len(s):
                    return True
        return False        
