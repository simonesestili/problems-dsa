class Solution:
    def clearStars(self, s):
        ans, indices = [], [[] for _ in range(26)]
        for c in s:
            if c != '*':
                indices[ord(c) - ord('a')].append(len(ans))
                ans.append(c)
                continue
            for i in range(26):
                if indices[i]:
                    ans[indices[i].pop()] = '*'
                    break
        return ''.join(c for c in ans if c != '*')
