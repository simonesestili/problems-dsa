class Solution:
    def minMaxSubarraySum(self, nums, k):
        n = len(nums)

        lmnuses, lmxuses = [0] * n, [0] * n
        mn, mx = [(-1, -inf)], [(-1, inf)]
        for i in range(n):
            while mn[-1][1] >= nums[i]:
                mn.pop()
            while mx[-1][1] <= nums[i]:
                mx.pop()
            lmnuses[i] = min(k, i - mn[-1][0])
            lmxuses[i] = min(k, i - mx[-1][0])
            mn.append((i, nums[i]))
            mx.append((i, nums[i]))

        rmnuses, rmxuses = [0] * n, [0] * n
        mn, mx = [(n, -inf)], [(n, inf)]
        for i in range(n - 1, -1, -1):
            while mn[-1][1] > nums[i]:
                mn.pop()
            while mx[-1][1] < nums[i]:
                mx.pop()
            rmnuses[i] = min(k, mn[-1][0] - i)
            rmxuses[i] = min(k, mx[-1][0] - i)
            mn.append((i, nums[i]))
            mx.append((i, nums[i]))

        summ = lambda x: (x*x + x) // 2 if x > 0 else 0
        ans = 0
        for i, x in enumerate(nums):
            l, r = lmnuses[i], rmnuses[i]
            ans += x * (l * r - summ(l + r - 1 - k))

            l, r = lmxuses[i], rmxuses[i]
            ans += x * (l * r - summ(l + r - 1 - k))

        return ans
