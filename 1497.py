class Solution:
    def canArrange(self, arr, k):
        mods = defaultdict(int)
        for x in arr:
            mods[x % k] += 1
        for mod in mods:
            comp = (k - mod) % k
            if comp == mod and mods[mod] % 2 or mods[comp] != mods[mod]:
                return False
            mods[mod], mods[comp] = 0, 0
        return True
