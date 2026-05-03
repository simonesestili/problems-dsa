class Solution:
    def rotateString(self, s, goal):
        return len(goal) == len(s) and goal in s+s
