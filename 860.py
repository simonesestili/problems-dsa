class Solution:
    def lemonadeChange(self, bills):
        fives = tens = 0
        for x in bills:
            if x == 5:
                fives += 1
            elif x == 10:
                tens += 1
                fives -= 1
            elif x == 20 and tens:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
            if fives < 0: return False
        return True

