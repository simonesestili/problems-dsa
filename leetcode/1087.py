class Solution:
    def expand(self, s):
        expansions, options, stack = [], [], []
        nested = False
        for i, c in enumerate(s):
            if c == '{':
                stack.append(i)
                nested = True
            elif c == '}':
                options.append(sorted(s[stack.pop()+1:i].split(',')))
                nested = False
            elif not nested:
                options.append([c])

        curr = []
        def dfs(i):
            if i == len(options):
                expansions.append(''.join(curr))
                return
            for c in options[i]:
                curr.append(c)
                dfs(i+1)
                curr.pop()

        dfs(0)
        return expansions
