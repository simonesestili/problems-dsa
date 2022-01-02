class Solution:
    def numberOfBeams(self, bank):
        count, bank = 0, [row.count('1') for row in bank if row.count('1')]
        for i in range(1, len(bank)):
            count += bank[i] * bank[i - 1]
        return count
