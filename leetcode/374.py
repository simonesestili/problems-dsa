class Solution:
    # Just do binary search eliminating (right - left) // 2 elemets at each guess
    def guessNumber(self, n):
        left, right = 1, n
        while True:
            mid = (left + right) // 2
            response = guess(mid)
            if response == -1:
                right = mid - 1
            elif response == 1:
                left = mid + 1
            else:
                return mid
