class Solution:
    def calPoints(self, ops):
        record = []

        for op in ops:
            if op == '+': record.append(record[-1] + record[-2])
            elif op == 'D': record.append(2 * record[-1])
            elif op == 'C': record.pop()
            else: record.append(int(op))

        return sum(record)
