class Solution:
    def generate(self, k):
        ans = [[1]]
        for r in range(2, k+1):
            ans.append([ans[-1][i-1]+ans[-1][i] if 0<i<r-1 else 1 for i in range(r)])
        return ans
