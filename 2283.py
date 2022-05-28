class Solution:
    def digitCount(self, num):
        for i, d in enumerate(num):
            if num.count(str(i)) != int(d):
                return False
        return True
