class Solution:
    def groupThePeople(self, sizes):
        ans, groups = [], defaultdict(list)
        for i, size in enumerate(sizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = []
        return ans
