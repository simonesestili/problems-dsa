class Solution:
    def minimumNumbers(self, num, k):
        if not num: return 0
        curr = count = valid = 0
        for _ in range(16):
            curr += k
            count += 1
            if curr % 10 == num % 10:
                valid = 1
                break
        if not valid or curr > num: return -1
        return count

