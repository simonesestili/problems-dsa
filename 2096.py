class Solution:
    def getDirections(self, root, s, d):
        
        def dfs(node, moves, t):
            if node is None: return
            if node.val == t: return moves
            moves.append('L')
            if dfs(node.left, moves, t): return moves
            moves.pop()
            moves.append('R')
            if dfs(node.right, moves, t): return moves
            moves.pop()

        spath = dfs(root, [], s)
        dpath = dfs(root, [], d)

        i = 0
        while i < min(len(spath), len(dpath)) and spath[i] == dpath[i]:
            i += 1

        return 'U' * (len(spath) - i) + ''.join(dpath[i:])

