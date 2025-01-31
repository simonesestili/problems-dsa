class Solution:
    def partitionLabels(self, s):
        ans, rightmost = [], {c: i for i, c in enumerate(s)}

        counted, bound = 0, rightmost[s[0]]
        for i, c in enumerate(s):
            bound = max(bound, rightmost[c])
            if bound == i:
                ans.append(i + 1 - counted)
                counted += ans[-1]

        return ans
