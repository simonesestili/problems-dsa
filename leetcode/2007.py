class Solution:
    def findOriginalArray(self, changed):
        counts = Counter(changed)
        if counts[0] % 2: return []
        ans = [0] * (counts[0] // 2)

        for x in sorted(counts.keys(), reverse=True):
            if x == 0 or counts[x] == 0: continue
            if x % 2 or counts[x//2] < counts[x]: return []
            ans.extend([x//2] * counts[x])
            counts[x//2] -= counts[x]

        return ans
