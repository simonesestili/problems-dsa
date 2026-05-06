class Solution:
    def rotateTheBox(self, box):
        box = [list(row) for row in zip(*box[::-1])]

        m, n = len(box), len(box[0])
        for c in range(n):
            top = 0
            for r in range(m):
                if box[r][c] == '*':
                    top = r+1
                if box[r][c] == '.':
                    box[top][c], box[r][c] = box[r][c], box[top][c]
                    top += 1

        return box
