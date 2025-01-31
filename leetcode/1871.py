class Solution:
    def canReach(self, s, mn, mx):
        reachable = [i == 0 for i in range(len(s))]
        
        count = 0
        for i in range(mn, len(s)):
            count += reachable[i - mn]
            left = i - mx - 1
            if left >= 0: count -= reachable[left]
            reachable[i] = count > 0 and s[i] == '0'

        return reachable[-1]
