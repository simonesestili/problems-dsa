class Solution:
    def numTilePossibilities(self, tiles):
        n = len(tiles)
        curr, seen = [], set()
        def dfs(mask):
            for i in range(n):
                if mask >> i & 1:
                    curr.append(tiles[i])
                    seen.add(''.join(curr))
                    dfs(mask - (1 << i))
                    curr.pop()

        dfs((1 << n) - 1)
        return len(seen)

