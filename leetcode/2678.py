class Solution:
    def countSeniors(self, details):
        return sum(int(d[11:13]) > 60 for d in details)

