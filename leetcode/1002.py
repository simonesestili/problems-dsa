class Solution:
    def commonChars(self, words):
        chars = reduce(and_, map(Counter, words))
        return [c for c, count in chars.items() for _ in range(count)]

