class Solution:
    def canConstruct(self, s, k):
        return len(s) >= k and k >= sum(cnt % 2 for cnt in Counter(s).values())
