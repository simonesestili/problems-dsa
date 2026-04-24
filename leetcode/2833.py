class Solution:
    def furthestDistanceFromOrigin(self, moves):
        cnts = Counter(moves)
        return abs(cnts['R'] - cnts['L']) + cnts['_']
