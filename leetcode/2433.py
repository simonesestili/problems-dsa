class Solution:
    def findArray(self, pref):
        arr = pref.copy()
        for i in range(1, len(arr)):
            arr[i] = pref[i] ^ pref[i-1]
        return arr
