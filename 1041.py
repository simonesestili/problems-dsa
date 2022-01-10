class Solution:
    def isRobotBounded(self, s):
        x = y = face = 0
        for c in s:
            if c == 'L': face = (face - 1) % 4
            elif c == 'R': face = (face + 1) % 4
            elif face == 0: y += 1
            elif face == 1: x += 1
            elif face == 2: y -= 1
            elif face == 3: x -= 1
        return not x and not y or face
