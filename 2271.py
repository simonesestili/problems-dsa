class Solution:
    def maximumWhiteTiles(self, tiles, carpet):
        n, tiles = len(tiles), sorted(tiles)
        prefix = [0] + list(accumulate([r - l + 1 for l, r in tiles]))

        best = 0
        for i, (l, r) in enumerate(tiles):
            j = bisect_left(tiles, [l + carpet, float('-inf')]) - 1
            cand = prefix[j] - prefix[i]
            rightmost = l + carpet - 1
            cand += min(tiles[j][1] - tiles[j][0] + 1, rightmost - tiles[j][0] + 1)
            best = max(best, cand)

        return best
