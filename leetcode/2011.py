class Solution:
    def finalValueAfterOperations(self, ops):
        return sum(1 if '++' in op else -1 for op in ops)
