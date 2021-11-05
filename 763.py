class Solution:
    def partitionLabels(self, s):
        ans = []
        rightmost = {}
        for i, c in enumerate(s):
            rightmost[c] = i
        left, right = 0, rightmost[s[0]]
        for i, c in enumerate(s):
            if not i: continue
            if i == right + 1:
                ans.append(right - left + 1)
                left = i
            right = max(right, rightmost[c])
        return ans + [len(s) - left]
