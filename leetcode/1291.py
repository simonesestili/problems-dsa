class Solution:
    def sequentialDigits(self, lo, hi):
        ans = []
        start, end = len(str(lo)), len(str(hi))
        for i in range(start, end + 1):
            for j in range(1, 11 - i):
                num = self.build(j, i)
                if lo <= num <= hi:
                    ans.append(num)
        return ans

    def build(self, first, length):
        return int(''.join([str(i) for i in range(first, first + length)]))
