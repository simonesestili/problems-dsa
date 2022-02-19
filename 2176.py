class Solution:
    def countPairs(self, nums, k):
        ans, seen = 0, defaultdict(list)

        for i, x in enumerate(nums):
            for j in seen[x]:
                ans += (i * j) % k == 0
            seen[x].append(i)

        return ans
