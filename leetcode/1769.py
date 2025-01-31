class Solution:
    def minOperations(self, boxes):
        lcnt = prefix = 0
        rcnt, suffix = boxes.count('1'), sum(i for i, b in enumerate(boxes) if b == '1')
        ans = []
        for b in boxes:
            ans.append(prefix + suffix)
            rcnt -= b == '1'
            suffix -= rcnt
            lcnt += b == '1'
            prefix += lcnt
        return ans
