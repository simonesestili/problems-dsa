class Solution:
    def carFleet(self, target, pos, speed):
        pos.append(0); speed.append(0);
        self.cars = sorted(zip(pos, speed))
        n = len(self.cars)
        fleets, curr_lead = 0, n - 1 
        for i in range(n - 2, -1, -1):
            if not self.catches(i, curr_lead, target):
                fleets += 1
                curr_lead = i
        return fleets

    def catches(self, i, j, target):
        pi, si = self.cars[i]
        pj, sj = self.cars[j]
        time = (target - pj) / sj
        return pi + si * time >= target
