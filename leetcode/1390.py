class Solution:
    def sumFourDivisors(self, nums):
        ans = 0
        for x in nums:
            if sqrt(x) == int(sqrt(x)):
                continue
            s = cnt = 0
            for i in range(1, ceil(sqrt(x))):
                if x % i == 0:
                    s += i + x // i
                    cnt += 1
            if cnt == 2:
                ans += s
        return ans
