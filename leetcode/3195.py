class Solution:
    def minimumArea(self, grid):
        mnr = mnc = inf
        mxr = mxc = -inf
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    mnr = min(r, mnr)
                    mnc = min(c, mnc)
                    mxr = max(r, mxr)
                    mxc = max(c, mxc)
        return (mxc - mnc + 1) * (mxr - mnr + 1)
