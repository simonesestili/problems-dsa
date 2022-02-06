#Q3
class Bitset:
    def __init__(self, size: int):
        self.arr = [0] * size
        self.flips = False
        self.n = size
        self.cnt = 0

    def fix(self, idx: int) -> None:
        self.cnt += self.arr[idx] if self.flips else not self.arr[idx]
        self.arr[idx] = int(not self.flips)

    def unfix(self, idx: int) -> None:
        self.cnt -= self.arr[idx] if not self.flips else not self.arr[idx]
        self.arr[idx] = int(self.flips)

    def flip(self) -> None:
        self.flips = not self.flips
        self.cnt = self.n - self.cnt

    def all(self) -> bool:
        return self.cnt == self.n

    def one(self) -> bool:
        return self.cnt != 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return ''.join([str(x ^ 1 if self.flips else x) for x in self.arr])
