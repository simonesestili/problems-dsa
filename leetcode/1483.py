class TreeAncestor:
    def __init__(self, n, parent):
        self.max_k = int(log2(n)) + 1
        self.ancestors = [[parent[i] if k == 0 else -1 for k in range(self.max_k)] for i in range(n)]
        for k in range(1, self.max_k):
            for i in range(n):
                half = self.ancestors[i][k - 1]
                self.ancestors[i][k] = -1 if half == -1 else self.ancestors[half][k - 1]

    def getKthAncestor(self, node, k):
        for i in range(16):
            if k & (1 << i):
                if node == -1:
                    return -1
                node = self.ancestors[node][i]
        return node
