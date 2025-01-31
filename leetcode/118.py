class Solution:
    def generate(self, rows):
        ans, prev = [[1]], [1]
        for count in range(rows - 1):
            k = count + 2
            level = [1 if i in (0, k - 1) else prev[i] + prev[i - 1] for i in range(k)]
            ans.append(level)
            prev = level
        return ans    
