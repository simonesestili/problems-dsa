class Solution:
    def removeSubfolders(self, folder):
        folder.sort(key=lambda x: x.count('/'))

        seen = set()
        for path in folder:
            curr = ''
            for part in path.split('/')[1:]:
                curr += f'/{part}'
                if curr in seen:
                    break
            else:
                seen.add(curr)

        return list(seen)
