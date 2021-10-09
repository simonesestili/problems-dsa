class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        curr = self.trie
        for idx in range(len(word)):
            if word[idx] not in curr:
                curr[word[idx]] = {}
            curr = curr[word[idx]]
        curr['*'] = True    

class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        found = []
        trie = trie.trie

        def dfs(row, col, curr, trie):
            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] == '*':
                return
            letter = board[row][col]
            if letter not in trie:
                return
            curr += letter
            trie = trie[letter]
            if '*' in trie:
                del trie['*']
                found.append(curr)
            board[row][col] = '*'
            dfs(row + 1, col, curr, trie)    
            dfs(row - 1, col, curr, trie)    
            dfs(row, col + 1, curr, trie)    
            dfs(row, col - 1, curr, trie)    
            board[row][col] = letter

        for row in range(m):
            for col in range(n):
                dfs(row, col, '', trie)
        
        return found
