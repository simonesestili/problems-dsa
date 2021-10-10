class Solution:
    def minOperations(self, grid, x):
        vals = [val for row in grid for val in row]
        vals.sort()
        n = len(vals)
        # Check if it is possible to make univalue grid
        for val in vals:
            if (val - vals[0]) % x:
                return -1
        operations = 0
        median = vals[n // 2]
        for val in vals:
            diff = abs(median - val)
            operations += diff // x
        return operations    
