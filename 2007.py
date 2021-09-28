class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        changed.sort()
        seen = set()
        elems = defaultdict(list)
        for idx, e in enumerate(changed):
            elems[e].append(idx)
        original = []
        for i in range(n - 1, -1, -1):
            if len(seen) == n or len(original) == n / 2:
                return original
            if i in seen:
                continue
            seen.add(i)
            if changed[i] / 2 in elems:
                if len(elems[changed[i] / 2]) == 0:
                    return []
                seen.add(elems[changed[i] / 2].pop())
                original.append(changed[i] // 2)
            else:
                return []
        return original    
