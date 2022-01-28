class Solution:
    def nextGreaterElement(self, n):
        digs, indices = list(map(int, str(n))), {}
        m = len(digs)

        for i in range(m - 1, -1, -1):
            indices[digs[i]] = i
            for d in range(digs[i] + 1, 10):
                if d not in indices: continue
                ans = digs[:i] + [d] + sorted(digs[i:indices[d]] + digs[indices[d]+1:])
                ans = int(''.join(map(str, ans)))
                return ans if ans < 1 << 31 else -1

        return -1
                
