class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk
        for idx, student in enumerate(chalk):
            k -= student
            if k < 0:
                return idx
