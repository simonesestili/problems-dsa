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
            while True:
                _, i, j, a, b = pairs.pop(0)
                l = idxs.bisect_left((i, -inf))
                if l + 1 >= len(idxs) or idxs[l] != (i, a) or idxs[l+1] != (j, b):
                    continue
                break

            desc -= b < a
            L = idxs[l - 1] if l else None
            R = idxs[l + 2] if l + 2 < len(idxs) else None

            if L:
                desc -= a < L[1]
                pairs.add((L[1] + a + b, L[0], i, L[1], a + b))
                desc += a + b < L[1]
            if R:
                desc -= R[1] < b
                pairs.add((a + b + R[1], i, R[0], a + b, R[1]))
                desc += R[1] < a + b

            idxs.pop(l+1)
            idxs.pop(l)
            idxs.add((i, a + b))

            ans += 1

        return ans
