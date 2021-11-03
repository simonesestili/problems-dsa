class Solution:
    def generate(self, rows):
        ans = [[1]]
        if rows == 1: return ans
        prev = [1]
        for count in range(rows - 1):
            level = [1] * (count + 2)
            for i in range(1, len(level) - 1):
                level[i] = prev[i] + prev[i - 1]
            ans.append(level)
            prev = level
        return ans    
