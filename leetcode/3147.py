class Solution:
    def maximumEnergy(self, energy, k):
        ans, curr = -inf, [0] * k
        for i in range(len(energy) - 1, -1, -1):
            curr[i%k] += energy[i]
            ans = max(ans, curr[i%k])
        return ans
