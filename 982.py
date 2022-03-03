class Solution:
    def countTriplets(self, nums):
        n, ans = len(nums), 0

        pairs = defaultdict(int)
        for i in nums:
            for j in nums:
                pairs[i & j] += 1

        for num in nums:
            for pair in pairs:
                if num & pair == 0:
                    ans += pairs[pair]

        return ans
