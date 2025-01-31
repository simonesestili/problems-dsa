class Solution:
    def removeDuplicates(self, s):
        ans = []
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
