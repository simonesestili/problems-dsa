class Solution:
    def countCollisions(self, dirs):
        left = 0
        while left < len(dirs):
            if dirs[left] == 'L': left += 1
            else: break
        right = len(dirs) - 1
        while right > left:
            if dirs[right] == 'R': right -= 1
            else: break

        dirs = dirs[left:right+1]
        if len(dirs) <= 1: return 0

        ans = 0 
        rights = 0
        for d in dirs:
            if d == 'R': rights += 1
            if d == 'S':
                ans += rights
                rights = 0
            if d == 'L':
                ans += rights + 1
                rights = 0
        return ans

