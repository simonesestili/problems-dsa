class Solution:
    def numRabbits(self, answers):
        ans, groups = 0, defaultdict(int)
        for cnt in answers:
            if groups[cnt + 1] % (cnt + 1) == 0:
                ans += cnt + 1
            groups[cnt + 1] = (groups[cnt + 1] + 1) % (cnt + 1)
        return ans
