class Solution:
    def findLucky(self, arr):
        return max((v for v, cnt in Counter(arr).items() if v == cnt), default=-1)
