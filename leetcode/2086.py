class Solution:
    def minimumBuckets(self, street):
        n = len(street)
        ans = i = 0

        while i < len(street):
            if street[i] == 'H':
                if i+1 != n and street[i+1] == '.': i += 2
                elif not i or street[i-1] == 'H': return -1
                ans += 1
            i += 1

        return ans
