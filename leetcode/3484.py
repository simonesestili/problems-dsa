class Spreadsheet:
    def __init__(self, rows):
        self.vals = defaultdict(int)

    def setCell(self, cell, value):
        self.vals[cell] = value

    def resetCell(self, cell):
        self.vals[cell] = 0

    def getValue(self, formula):
        x, y = formula[1:].split('+')
        x = int(x) if x.isdigit() else self.vals[x]
        y = int(y) if y.isdigit() else self.vals[y]
        return x + y
