class Solution:
    def minMovesToMakePalindrome(self, s):
        moves, s = 0, list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
                continue
            temp = right
            while temp > left and s[temp] != s[left]:
                temp -= 1

            if temp == left:
                moves += 1
                s[left], s[left+1] = s[left+1], s[left]
            else:
                while s[right] != s[left]:
                    s[temp], s[temp+1] = s[temp+1], s[temp]
                    moves += 1
                    temp += 1
                left, right = left + 1, right - 1

        return moves
