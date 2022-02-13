class Solution:
    def minimumRemoval(self, beans): 
        n, beans, prefix = len(beans), sorted(beans), [0]
        for count in beans: prefix.append(prefix[-1] + count)
        ans = float('inf')
        for i, count in enumerate(beans):
            cand = prefix[i] + prefix[-1] - prefix[i] - (n - i) * count
            ans = min(ans, cand)
        return ans
