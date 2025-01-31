class Solution:
    def shortestWay(self, source, target):
        m, n = len(source), len(target)
        ans = i = 0
        
        while i < n:
            diff = 0
            for j in range(m):
                diff += i + diff < n and source[j] == target[i+diff]
            if not diff: return -1
            i += diff
            ans += 1

        return ans

