class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n, groups, idxs = len(nums), [], {}

        for x, i in sorted((x, i) for i, x in enumerate(nums)):
            if not groups or x - groups[-1][-1] > limit:
                groups.append(deque([x]))
            else:
                groups[-1].append(x)
            idxs[i] = len(groups) - 1

        for i in range(n):
            nums[i] = groups[idxs[i]].popleft()

        return nums
