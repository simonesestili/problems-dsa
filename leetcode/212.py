DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Trie(dict):
    def insert(self, word):
        curr = self
        for w in word:
            if w not in curr: curr[w] = {}
            curr = curr[w]
        curr['*'] = True

class Solution:
    def findWords(self, board, words):
        m, n, trie = len(board), len(board[0]), Trie()
        for w in words: trie.insert(w)

        ans, curr = [], []
        def dfs(row, col, node):
            c = board[row][col]
            if c not in node: return
            board[row][col] = '*'
            curr.append(c)
            if '*' in node[c]:
                ans.append(''.join(curr))
                board[row][col] = curr.pop()
                return
            for dr, dc in DIRS:
                dr, dc = row + dr, col + dc
                if 0 <= dr < m and 0 <= dc < n and board[dr][dc] != '*':
                    dfs(dr, dc, node[c])
            board[row][col] = curr.pop()

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return ans
            

