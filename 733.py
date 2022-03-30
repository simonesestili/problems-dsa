class Solution:
    def floodFill(self, img, sr, sc, col):
        m, n, start = len(img), len(img[0]), img[sr][sc]

        curr, seen = [(sr, sc)], set([(sr, sc)])
        while curr:
            nextt = []
            for r, c in curr:
                img[r][c] = col
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    dr, dc = r + dr, c + dc
                    if 0 <= dr < m and 0 <= dc < n and (dr, dc) not in seen and img[dr][dc] == start:
                        nextt.append((dr, dc))
                        seen.add((dr, dc))
            curr = nextt

        return img
