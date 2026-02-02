class Solution:
    def minimumCost(self, nums, k, dist):
        n, m = len(nums), k - 2
        self.lsum, left, right, = 0, SortedList(), SortedList()

        def fix():
            while len(left) > m:
                v = left.pop(-1)
                self.lsum -= v
                right.add(v)
            while len(left) < m and right:
                v = right.pop(0)
                left.add(v)
                self.lsum += v

        def add(x):
            if left and x > left[-1]:
                right.add(x)
            else:
                left.add(x)
                self.lsum += x
            fix()

        def remove(x):
            i = left.bisect_left(x)
            if i < len(left) and left[i] == x:
                self.lsum -= left.pop(i)
            else:
                right.remove(x)
            fix()

        for i in range(2, min(n, dist + 2)):
            add(nums[i])

        ans = inf
        for i in range(1, n - k + 2):
            ans = min(ans, nums[0] + nums[i] + self.lsum)
            remove(nums[i+1])
            if i + dist + 1 < n:
                add(nums[i + dist + 1])
        return ans
