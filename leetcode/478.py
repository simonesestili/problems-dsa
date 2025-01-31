class Solution:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def randPoint(self):
        deg = random() * 2 * pi
        r = sqrt(random()) * self.r
        x = r * cos(deg) + self.x
        y = r * sin(deg) + self.y
        return [x, y]
