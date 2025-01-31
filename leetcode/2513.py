MOD = 10 ** 9 + 7
class Solution:
    def countAnagrams(self, s):
        ans = 1
        for word in s.split(' '):
            counts, perms = Counter(word), factorial(len(word))
            for count in counts.values():
                perms //= factorial(count)
            ans = (ans * perms) % MOD
        return ans
