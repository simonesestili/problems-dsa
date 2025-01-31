class Solution:
    def removeAnagrams(self, words):
        ans = []
        for w in words:
            if not ans or sorted(ans[-1]) != sorted(w):
                ans.append(w)
        return ans
