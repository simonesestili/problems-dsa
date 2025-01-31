class Solution:
    def minSubarray(self, nums, p):
        n = len(nums)
        prefix, curr = [0] * n, 0
        for i in range(n):
            curr = (curr + nums[i]) % p
            prefix[i] = curr
        target = prefix[-1]
        seen, smallest = {0: -1}, n
        for i in range(n):
            seen[prefix[i]] = i
            if (prefix[i] - target) % p in seen:
                smallest = min(smallest, i - seen[(prefix[i] - target) % p])

        return -1 if smallest >= n else smallest
