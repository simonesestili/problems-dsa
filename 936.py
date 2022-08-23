class Solution:
    def movesToStamp(self, stamp, target):
        n, m = len(stamp), len(target)
        s, moves = list(target), []

        def removable(i):
            unstamp = False
            for j in range(i, i + n):
                if s[j] == '?': continue
                if s[j] != stamp[j-i]: return False
                unstamp = True
            return unstamp

        unseen = True
        while unseen:
            unseen = False
            for i in range(m - n + 1):
                if not removable(i): continue
                for j in range(i, i + n): s[j] = '?'
                moves.append(i)
                unseen = True

        return reversed(moves) if set(s) == {'?'} else []

