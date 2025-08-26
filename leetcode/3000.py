class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        return reduce(operator.mul, max(dimensions, key=lambda d: (d[0]*d[0]+d[1]*d[1], d[0]*d[1])))
