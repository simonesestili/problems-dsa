class Solution:
    def maximumEvenSplit(self, finalSum):
        if finalSum & 1: return []
        ans, i = [], 2

        while finalSum - i >= i + 2:
            ans.append(i)
            finalSum -= i
            i += 2

        ans.append(finalSum)
        return ans

