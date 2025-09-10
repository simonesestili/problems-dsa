class Solution:
    def minimumTeachings(self, n, languages, friendships):
        m, languages = len(languages), list(map(set, languages))

        missing = set()
        for u, v in friendships:
            if not languages[u-1] & languages[v-1]:
                missing.add(u)
                missing.add(v)

        cnts = defaultdict(int)
        for p in missing:
            for l in languages[p-1]:
                cnts[l] += 1

        return len(missing) - max(cnts.values(), default=0)
