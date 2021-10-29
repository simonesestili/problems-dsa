class Solution:
    def minimumPerimeter(self, target):
        apples = r = 0
        while apples < target:
            r += 1
            apples += 12 * (r ** 2)
        return r * 8
