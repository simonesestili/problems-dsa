class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        values = sorted(list(counter.values()))
        unique = len(values)
        for val in values:
            if val <= k:
                k -= val
                unique -= 1
            else:
                return unique
        return unique
        
