class Solution:
    def findThePrefixCommonArray(self, A, B):
        ans, seen, cnt = [], set(), 0
        for a, b in zip(A, B):
            cnt += a in seen
            seen.add(a)
            cnt += b in seen
            seen.add(b)
            ans.append(cnt)
        return ans
