from sortedcontainers import SortedList
class Solution:
    def longestRepeating(self, s, queries, indices):
        s, start, curr = list(s+'!'), 0, s[0]
        n, segments, sizes = len(s), SortedList(), SortedList()

        # BUILD SEGMENTS
        for i in range(1, n):
            if curr != s[i]:
                segments.add((start, i - 1)); sizes.add(i - start)
                start, curr = i, s[i]

        def split(a, b):
            i = segments.bisect_right((a, float('inf'))) - 1
            I = (segments[i][0], segments[i][1])
            sizes.remove(I[1] - I[0] + 1)
            segments.pop(i)
            segments.add((I[0], a)); segments.add((b, I[1]))
            sizes.add(a - I[0] + 1); sizes.add(I[1] - b + 1)

        def join(a, b):
            i = segments.bisect_right((a, float('inf'))) - 1
            j = segments.bisect_right((b, float('inf'))) - 1
            I, J = (segments[i][0], segments[i][1]), (segments[j][0], segments[j][1])
            sizes.remove(I[1] - I[0] + 1)
            sizes.remove(J[1] - J[0] + 1)
            segments.pop(i); segments.pop(i)
            segments.add((I[0], J[1]))
            sizes.add(J[1] - I[0] + 1)

        ans = []
        for c, i in zip(queries, indices):
            if c == s[i]:
                ans.append(sizes[-1])
                continue

            # LEFT SIDE
            if i and s[i-1] == s[i]: split(i - 1, i)
            elif i and s[i-1] == c: join(i - 1, i)

            # RIGHT SIDE
            if i < len(s) - 2 and s[i+1] == s[i]: split(i, i + 1)
            elif i < len(s) - 2 and s[i+1] == c: join(i, i + 1)
            
            s[i] = c
            ans.append(sizes[-1])

        return ans
