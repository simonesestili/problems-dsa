class Solution:
    def maximumBobPoints(self, num, alice):
        ans, best = [0] * 12, 0

        for mask in range(1 << 12):
            cand = [0] * 12
            score = used = 0
            for i in range(1, 12):
                if mask >> i & 1:
                    used += alice[i] + 1
                    score += i
                    cand[i] = alice[i] + 1
            if score > best and used <= num:
                ans = cand
                best = score

        ans[0] = num - sum(ans)
        return ans
