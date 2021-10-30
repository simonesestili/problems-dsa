class Solution:
    def minimumPerimeter(self, target):
        n = 1
        while True:
            if (n) * (n + 1) * (2 * n + 1) >= target / 2:
                return n * 8
            n += 1