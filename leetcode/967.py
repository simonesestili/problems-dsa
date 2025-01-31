class Solution:
    def numsSameConsecDiff(self, n, k):
		nums = []

        def fill(num, rem):
            if rem == 0:
                nums.append(num)
                return
            last = num % 10
            if last - k >= 0: fill(num * 10 + last - k, rem - 1)
            if last + k < 10 and k: fill(num * 10 + last + k, rem - 1)

        for start in range(1, 10):
            fill(start, n - 1)
        return nums

