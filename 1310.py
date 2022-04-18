class Solution:
    def xorQueries(self, arr, queries):
        prefix = [0]
        for x in arr: prefix.append(prefix[-1] ^ x)

        return [prefix[r+1] ^ prefix[l] for l, r in queries]
