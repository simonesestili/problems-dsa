class Solution:
    def numberOfBeams(self, bank):
        bank = [row.count('1') for row in bank if row.count('1')]
        if len(bank) < 2: return 0
        count, n = 0, len(bank)
        for i in range(1, n):
            count += bank[i] * bank[i - 1]
        return count

