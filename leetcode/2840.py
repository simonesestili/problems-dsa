class Solution:
    def checkStrings(self, a, b):
        return not Counter(a[::2]) - Counter(b[::2]) and not Counter(a[1::2]) - Counter(b[1::2])
