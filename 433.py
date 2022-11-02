class Solution:
    def minMutation(self, start, end, bank):
        def neighs(gene):
            for i in range(8):
                for x in 'ACGT':
                    yield gene[:i] + x + gene[i+1:]

        queue, seen = deque([(0, start)]), set([start])
        while queue:
            mutations, gene = queue.popleft()
            if gene == end: return mutations
            for neigh in neighs(gene):
                if neigh not in bank or neigh in seen: continue
                queue.append((mutations + 1, neigh))
                seen.add(neigh)
        return -1
