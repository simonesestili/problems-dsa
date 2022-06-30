class Solution:
    def reconstructQueue(self, people):
        ans = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            ans.insert(k, (h, k))
        return ans
