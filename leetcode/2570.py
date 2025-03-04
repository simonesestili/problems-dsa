class Solution:
    def mergeArrays(self, a, b):
        ans = []
        m, n, i, j = len(a), len(b), 0, 0
        while i < m or j < n:
            if j >= n or i < m and a[i] < b[j]:
                id, val = a[i]
                i += 1
            else:
                id, val = b[j]
                j += 1
            if not ans or ans[-1][0] != id:
                ans.append([id, 0])

            ans[-1][1] += val

        return ans
