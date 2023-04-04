class Solution:
    def partitionString(self, s):
        total, curr = 1, set()
        for c in s:
            if c in curr:
                curr.clear()
                total += 1
            curr.add(c)
        return total
