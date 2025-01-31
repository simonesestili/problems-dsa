class Solution:
    def maxSumTwoNoOverlap(self, nums, first, second):
        n = len(nums)

        def compute(k):
            res = [0] * n
            curr = sum(nums[-k:])
            best = curr
            res[-k] = best
            j = n - 1
            for i in range(n - k - 1, 0, -1):
                curr -= nums[j]
                j -= 1
                curr += nums[i]
                best = max(best, curr)
                res[i] = best
            return res

        # compute best subarray of len first starting at i or to the right
        max_first = compute(first)
        # compute best subarray of len second starting at i or to the right
        max_second = compute(second)

        ans = 0
        # check cases where first subarray is before the second one
        curr = sum(nums[:first])
        ans = curr + max_second[first]
        j = 0
        for i in range(first, n - second):
            curr -= nums[j]
            j += 1
            curr += nums[i]
            ans = max(ans, curr + max_second[i + 1])
        # check cases where first subarray is after the second one
        curr = sum(nums[:second])
        ans = max(ans, curr + max_first[second])
        j = 0
        for i in range(second, n - first):
            curr -= nums[j]
            j += 1
            curr += nums[i]
            ans = max(ans, curr + max_first[i + 1])
        return ans
