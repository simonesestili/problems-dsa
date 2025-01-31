class Solution:
    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        rep = tuple(mat[i//n][i%n] for i in range(m*n))

        def neighbors(rep):
            res = []
            for i in range(m*n):
                neigh = list(rep)
                neigh[i] ^= 1
                if i - n >= 0: neigh[i - n] ^= 1
                if i + n < m*n: neigh[i + n] ^= 1
                if i % n and n > 1: neigh[i - 1] ^= 1
                if i % n != n - 1 and n > 1: neigh[i + 1] ^= 1
                res.append(tuple(neigh))
            return res

        queue, seen = deque([(rep, 0)]), set([rep])
        while queue:
            curr, steps = queue.popleft()
            if not any(curr): return steps
            for neigh in neighbors(curr):
                if neigh in seen: continue
                queue.append((neigh, steps + 1))
                seen.add(neigh)

        return -1
