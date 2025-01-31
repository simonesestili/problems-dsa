class Solution:
    def eliminateMaximum(self, dist, speed):
        time = sorted([d / s for d, s in zip(dist, speed)])

        kills = 0
        for charged, t in enumerate(time):
            if t <= charged: break
            kills += 1
        return kills
