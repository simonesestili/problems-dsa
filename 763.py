class Solution:
    def partitionLabels(self, s):
        ans = []
        rightmost = {}
        for i, c in enumerate(s):
            rightmost[c] = i
