class Solution:
    def threeSumMulti(self, arr, target):
        ans, MOD = 0, pow(10, 9) + 7
        left, right = Counter(), Counter(arr)
        lvals = set()

        for x in arr:
            right[x] -= 1
            for lval in lvals:
                rval = target - lval - x
                ans = (ans + left[lval] * right[rval]) % MOD
            left[x] += 1
            lvals.add(x)

        return ans
