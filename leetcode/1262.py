class Solution:
    def maxSumDivThree(self, nums):
        s, vals = sum(nums), defaultdict(list)
        for x in sorted(nums):
            vals[x % 3].append(x)

        rem = 0
        if s % 3 == 1:
            a = vals[1][0] if len(vals[1]) >= 1 else inf
            b = vals[2][0] + vals[2][1] if len(vals[2]) >= 2 else inf
            rem = min(a, b)
        elif s % 3 == 2:
            a = vals[2][0] if len(vals[2]) >= 1 else inf
            b = vals[1][0] + vals[1][1] if len(vals[1]) >= 2 else inf
            rem = min(a, b)

        return s - rem
