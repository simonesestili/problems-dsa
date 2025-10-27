class Solution:
    def numberOfBeams(self, bank):
        cnts = [row.count('1') for row in bank if row.count('1')]
        return sum(cnts[i] * cnts[i+1] for i in range(len(cnts)-1))
