class Solution:
    def largestInteger(self, num):
        s = str(num)
        odds, evens = sorted([x for x in s if int(x) & 1]), sorted([x for x in s if not (int(x) & 1)])
        ans = []

        for x in s:
            if int(x) & 1:
                ans.append(odds.pop())
            else:
                ans.append(evens.pop())

        return int(''.join(ans))


