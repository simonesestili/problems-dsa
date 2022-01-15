class Solution:
    def minJumps(self, arr):
        n, seen, seen_nums, queue, nums = len(arr), set([0]), set(), deque([(0, 0)]), defaultdict(list)
        for i, x in enumerate(arr): nums[x].append(i)

        while queue:
            i, cost = queue.popleft()
            if i == n - 1: return cost

            for j in [i - 1, i + 1]:
                if 0 <= j < n and j not in seen:
                    queue.append((j, cost + 1))
                    seen.add(j)

            if arr[i] in seen_nums: continue
            for j in nums[arr[i]]:
                queue.append((j, cost + 1))
                seen.add(j)
            seen_nums.add(arr[i])

        return -1

