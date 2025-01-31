class Solution:
    def minimumSum(self, num):
         digs = sorted(str(num))
         return int(digs[0] + digs[2]) + int(digs[1] + digs[3])
