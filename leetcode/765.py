class Solution:
    def minSwapsCouples(self, row):
        n = len(row)
        ans = 0
        for i in range(0, n, 2):
            if row[i] // 2 == row[i+1] // 2: continue
            for j in range(i + 2, n):
                if row[j] == row[i] ^ 1: break
            row[i+1], row[j] = row[j], row[i+1]
            ans += 1
        return ans
