class Solution:
    def pushDominos(self, dominos):
        n, seen, is_right = len(dominos), [], False
        for d in dominos:
