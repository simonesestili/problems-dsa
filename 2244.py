class Solution:
    def minimumRounds(self, tasks):
        return -1 if 1 in (vs := Counter(tasks).values()) else sum(cnt // 3 + (cnt % 3 > 0) for cnt in vs)
