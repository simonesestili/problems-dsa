class Solution:
    def minimumPairRemoval(self, nums):
        n, pairs, idxs = len(nums), SortedList(), SortedList()
        ans = desc = 0

        for i in range(n - 1):
            desc += nums[i+1] < nums[i]
            pairs.add((nums[i] + nums[i+1], i, i+1, nums[i], nums[i+1]))
            idxs.add((i, nums[i]))
        idxs.add((n-1, nums[-1]))

        while desc:
            _, i, j, a, b = pairs.pop(0)
            desc -= b < a

            l = idxs.bisect_left((i, -inf))
            if l:
                pairs.remove((idxs[l-1][1] + a, idxs[l-1][0], i, idxs[l-1][1], a))
                desc -= a < idxs[l-1][1]
                pairs.add((idxs[l-1][1] + a + b, idxs[l-1][0], i, idxs[l-1][1], a + b))
                desc += a + b < idxs[l-1][1]

            r = idxs.bisect_right((j, inf))
            if r < len(idxs):
                pairs.remove((b + idxs[r][1], j, idxs[r][0], b, idxs[r][1]))
                desc -= idxs[r][1] < b
                pairs.add((a + b + idxs[r][1], i, idxs[r][0], a + b, idxs[r][1]))
                desc += idxs[r][1] < a + b

            idxs.pop(r-1)
            idxs.pop(l)
            idxs.add((i, a + b))

            ans += 1

        return ans
