class Solution:
    def missingRolls(self, rolls, mean, n):
        k = n + len(rolls)
        missing_sum = (mean * k) - sum(rolls)
        if missing_sum < n or missing_sum > n * 6:
            return []
        avg = int(math.ceil(missing_sum / n))
        obs = []
        for i in range(n):
            if (n - i) * (avg - 1) == missing_sum:
                return obs + [avg - 1] * (n - i)
            obs.append(avg)
            missing_sum -= avg
        return obs    

