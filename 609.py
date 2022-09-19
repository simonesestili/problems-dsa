class Solution:
    def findDuplicate(self, paths):
        groups = defaultdict(list)
        for folder, files in map(lambda x: x.split(' ', 1), paths):
            for file in files.split(' '):
                name, content = file.split('(')
                groups[content].append(f'{folder}/{name}')
        return [x for x in groups.values() if len(x) > 1]
