class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = defaultdict(set)
        for row, label in reservedSeats: rows[row].add(label)

        ans = n * 2
        LEFT, MID, RIGHT = {2,3,4,5}, {4,5,6,7}, {6,7,8,9}
        for row in rows:
            removed = 0
            if rows[row] & LEFT:
                removed += 1
                ans -= 1
            if rows[row] & RIGHT:
                removed += 1
                ans -= 1
            if removed == 2 and not rows[row] & MID:
                ans += 1

        return ans
