class Solution:
    def maximumNumber(self, num, change):
        num, j = [int(d) for d in num], len(num)
        for i, dig in enumerate(num):
            if change[dig] > dig:
                num[i] = change[dig]
                j = i + 1
                break
        while j < len(num) and change[num[j]] >= num[j]:
            num[j] = change[num[j]]
            j += 1
        return ''.join(map(str, num))
