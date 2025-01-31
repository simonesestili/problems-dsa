class Solution:
    def countPairs(self, nums, k):
        pairs, counts = 0, Counter([gcd(x, k) for x in nums])

        for i in counts:
            for j in counts:
                if i > j or i * j % k: continue
                pairs += counts[i] * counts[j] if i != j else counts[i] * (counts[i] - 1) // 2

        return pairs
