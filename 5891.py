class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        least, most = n, n * 6
        total = sum(rolls)
        target = (n + len(rolls)) * mean
        missing = target - total
        if missing < least or missing > most:
            return []
        num = missing // n
        ans = []
        while len(ans) < n:
            if (num + 1) * (n - len(ans)) == missing:
                while len(ans) < n:
                    ans.append(num+1)
                return ans
            missing -= num
            ans.append(num)
        return ans    