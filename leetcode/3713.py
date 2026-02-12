class Solution:
    def longestBalanced(self, s):
        n, ans = len(s), 0
        for i in range(n):
            cnts, uniq, cnt, mx = [0] * 26, 0, 0, 0
            for j in range(i, n):
                cnts[ord(s[j])-ord('a')] += 1
                uniq += cnts[ord(s[j])-ord('a')] == 1
                if cnts[ord(s[j])-ord('a')] > mx:
                    mx, cnt = cnts[ord(s[j])-ord('a')], 0
                cnt += cnts[ord(s[j])-ord('a')] == mx
                if uniq == cnt:
                    ans = max(ans, j - i + 1)
        return ans
