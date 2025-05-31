class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        def getpos(cell):
            cell -= 1
            return n - 1 - cell // n, n - cell % n - 1 if cell // n % 2 else cell % n

        q, seen = deque([(1, 0)]), set([1])
        while q:
            cell, moves = q.popleft()
            for nxt in range(cell + 1, min(cell + 6, n * n) + 1):
                r, c = getpos(nxt)
                nxt = board[r][c] if board[r][c] != -1 else nxt
                if nxt == n * n: return moves + 1
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, moves + 1))

        return -1

