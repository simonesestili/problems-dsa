class Solution:
    def knightDialer(self, n):
        paths = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        prev, curr = [1] * 10, [0] * 10
        for _ in range(n - 1):
            for end in range(10):
                ways = 0
                for path in paths[end]:
                    ways += prev[path]
                curr[end] = ways    
            prev, curr = curr, [0] * 10    
        return sum(prev) % (10 ** 9 + 7)
