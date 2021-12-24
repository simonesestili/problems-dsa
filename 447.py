class Solution:
    def numberOfBoomerangs(self, points):
        n, count = len(points), 0
        for i in range(n):
            dists = defaultdict(int)
            for j in range(n):
                dists[self.dist(points[i], points[j])] += 1
            for k in dists.values():
                count += k * k - k
        return count
        
    def dist(self, p1, p2):
        return pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2)
