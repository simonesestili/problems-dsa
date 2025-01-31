class Solution:     
    def findAnagrams(self, s, p):
        ans, m, n = [], len(s), len(p)
        if n > m: return ans

        target, curr = [0] * 26, [0] * 26
        for c in p: target[ord(c) - ord('a')] += 1
        for i in range(n - 1): curr[ord(s[i]) - ord('a')] += 1

        for i in range(n - 1, m):
            curr[ord(s[i]) - ord('a')] += 1
            if curr == target: ans.append(i - n + 1)
            curr[ord(s[i - n + 1]) - ord('a')] -= 1

        return ans

