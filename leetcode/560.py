class Solution:
    def subarraySum(self, nums, k):
        prefix, count, curr = defaultdict(int), 0, 0
        prefix[0] = 1

        for x in nums:
            curr += x
            count += prefix[curr - k]
            prefix[curr] += 1

        return count

